
from functools import reduce
import operator
from typing import Tuple, Dict, Sequence, Optional, List

from ..data import data_ops as e
from ..data import expr_ops as eops
from ..data import type_ops as tops
from edb.common import debug
from ..data import path_factor as path_factor
from .dml_checking import *
from ..data import expr_to_str as pp
from .function_checking import *


def synthesize_type_for_val(val: e.Val) -> e.Tp:
    match val:
        case e.ScalarVal(tp, v):
            return tp
        case _:
            raise ValueError("Not implemented", val)


def check_shape_transform(ctx: e.TcCtx, s: e.ShapeExpr,
                          tp: e.Tp
                          ) -> Tuple[e.Tp, e.ShapeExpr]:
    s_tp: e.ObjectTp
    l_tp: e.ObjectTp
    s_name: e.QualifiedName
    # populate result skeleton
    match tp:
        case e.NominalLinkTp(name=name, subject=subject_tp, linkprop=linkprop_tp):
            assert isinstance(name, e.QualifiedName), "should have been resolved"
            l_tp = linkprop_tp
            s_name = name
            if isinstance(subject_tp, e.ObjectTp):
                s_tp = subject_tp
            # elif isinstance(subject_tp, e.VarTp):
            #     s_tp = tops.dereference_var_tp(ctx.schema, subject_tp)
            else:
                raise ValueError("NI", subject_tp)
        case e.NamedNominalLinkTp(name=name, linkprop=linkprop_tp):
            assert isinstance(name, e.QualifiedName), "should have been resolved"
            l_tp = linkprop_tp
            s_name = name
            s_tp = tops.dereference_var_tp(ctx.schema, name)
        case e.ObjectTp(_):
            s_tp = tp
            l_tp = e.ObjectTp({})
            raise ValueError("Cannot get s_name")
        case _:
            raise ValueError("NI")

    result_s_tp = e.ObjectTp({})
    result_l_tp = e.ObjectTp({})
    result_expr = e.ShapeExpr({})

    for lbl, comp in s.shape.items():
        match lbl:
            case e.StrLabel(s_lbl):
                if s_lbl in s_tp.val.keys():
                    new_ctx, body, bnd_var = eops.tcctx_add_binding(
                        ctx, comp, e.ResultTp(tp, e.CardOne))
                    result_tp = s_tp.val[s_lbl]
                    body_tp_synth, body_ck = synthesize_type(new_ctx, body)
                    # if is_insert_shape:
                    #     tops.assert_insert_subtype(
                    #         ctx, body_tp_synth.tp, result_tp.tp)
                    # else:
                    #     tops.assert_shape_subtype(
                    #         ctx, body_tp_synth.tp, result_tp.tp)
                    tops.assert_cardinal_subtype(
                        body_tp_synth.mode, result_tp.mode)
                    result_s_tp = e.ObjectTp({**result_s_tp.val,
                                              s_lbl: body_tp_synth})
                    result_expr = e.ShapeExpr(
                        {**result_expr.shape,
                         lbl: eops.abstract_over_expr(body_ck, bnd_var)})
                else:
                    new_ctx, body, bnd_var = eops.tcctx_add_binding(
                        ctx, comp, e.ResultTp(tp, e.CardOne))
                    result_tp, checked_body = synthesize_type(
                        new_ctx, body)
                    result_s_tp = e.ObjectTp({**result_s_tp.val,
                                              s_lbl: result_tp})
                    result_expr = e.ShapeExpr(
                        {**result_expr.shape,
                         lbl: eops.abstract_over_expr(checked_body, bnd_var)})
            case e.LinkPropLabel(l_lbl):
                if l_lbl in l_tp.val.keys():
                    new_ctx, body, bnd_var = eops.tcctx_add_binding(
                        ctx, comp, e.ResultTp(tp, e.CardOne))
                    result_tp = l_tp.val[l_lbl]
                    body_synth_tp, body_ck = synthesize_type(new_ctx, body)
                    # if is_insert_shape:
                    #     tops.assert_insert_subtype(
                    #         ctx, body_synth_tp.tp, result_tp.tp)
                    # else:
                    #     tops.assert_shape_subtype(
                    #         ctx, body_synth_tp.tp, result_tp.tp)
                    # tops.assert_cardinal_subtype(
                    #     body_synth_tp.mode, result_tp.mode)
                    result_l_tp = e.ObjectTp({**result_l_tp.val,
                                              l_lbl: body_synth_tp})
                    result_expr = e.ShapeExpr(
                        {**result_expr.shape,
                         lbl: eops.abstract_over_expr(body_ck, bnd_var)})
                else:
                    new_ctx, body, bnd_var = eops.tcctx_add_binding(
                        ctx, comp, e.ResultTp(tp, e.CardOne))
                    result_tp, checked_body = synthesize_type(
                        new_ctx, body)
                    result_l_tp = e.ObjectTp({**result_l_tp.val,
                                              l_lbl: result_tp})
                    result_expr = e.ShapeExpr(
                        {**result_expr.shape,
                         lbl: eops.abstract_over_expr(checked_body, bnd_var)})

    for t_lbl, s_comp_tp in s_tp.val.items():
        if e.StrLabel(t_lbl) not in s.shape.keys():
            result_s_tp = e.ObjectTp({**result_s_tp.val,
                                      t_lbl: s_comp_tp})

    for t_lbl, l_comp_tp in l_tp.val.items():
        if e.LinkPropLabel(t_lbl) not in s.shape.keys():
            result_l_tp = e.ObjectTp({**result_l_tp.val,
                                      t_lbl: l_comp_tp})

    return e.NominalLinkTp(subject=result_s_tp, name=s_name, linkprop=result_l_tp), result_expr


def type_cast_tp(ctx: e.TcCtx, from_tp: e.ResultTp, to_tp: e.Tp) -> e.ResultTp:
        # match from_tp.tp, from_tp.mode, to_tp:
        # case e.UnifiableTp(id=_, resolution=None), card, _:
        #     assert isinstance(from_tp.tp, e.UnifiableTp)  # for mypy
        #     from_tp.tp.resolution = to_tp
        #     return e.ResultTp(to_tp, card)

        # case e.IntTp(), card, e.IntTp():
        #     return e.ResultTp(e.IntTp(), card)
        # case e.UuidTp(), card, e.StrTp():
        #     return e.ResultTp(e.StrTp(), card)
        # case e.IntTp(), card, e.StrTp():
        #     return e.ResultTp(e.StrTp(), card)
        if (from_tp.tp, to_tp) in ctx.schema.casts:
            return e.ResultTp(to_tp, from_tp.mode)
        else:
            raise ValueError("Not Implemented", from_tp, to_tp)


def synthesize_type(ctx: e.TcCtx, expr: e.Expr) -> Tuple[e.ResultTp, e.Expr]:
    result_tp: e.Tp
    result_card: e.CMMode
    result_expr: e.Expr = expr  # by default we don't change expr

    match expr:
        case (e.ScalarVal(_)):
            result_tp = synthesize_type_for_val(expr)
            result_card = e.CardOne
        case e.FreeVarExpr(var=var):
            if var in ctx.varctx.keys():
                result_tp, result_card = ctx.varctx[var]
            else:
                possible_resolved_name = mops.try_resolve_simple_name(ctx, e.UnqualifiedName(var))
                if possible_resolved_name is not None:
                    module_entity = mops.try_resolve_module_entity(ctx, possible_resolved_name)
                    match module_entity:
                        case e.ModuleEntityTypeDef(typedef=typedef):
                            assert isinstance(typedef, e.ObjectTp), "Cannot select Scalar type"
                            result_tp = e.NominalLinkTp(subject=typedef,
                                                        name=possible_resolved_name, 
                                                        linkprop=e.ObjectTp({}))
                            result_expr = possible_resolved_name
                            result_card = e.CardAny
                        case _:
                            raise ValueError("Unsupported Module Entity", module_entity)
                else:
                    raise ValueError("Unknown variable", var,
                                    "list of known vars",
                                    list(ctx.varctx.keys()))
        case e.TypeCastExpr(tp=tp, arg=arg):
            tp_ck = check_type_valid(ctx, tp)
            if expr_tp_is_not_synthesizable(arg):
                result_card, result_expr = check_type_no_card(ctx, arg, tp_ck)
                result_tp = tp_ck
            else:
                (arg_tp, arg_v) = synthesize_type(ctx, arg)
                if (arg_tp.tp, tp_ck) in ctx.schema.casts:
                # (result_tp, result_card) = type_cast_tp(ctx, arg_tp, tp_ck)
                    (result_tp, result_card) = (tp_ck, arg_tp.mode)
                    result_expr = e.CheckedTypeCastExpr(
                        cast_tp=(arg_tp.tp, tp_ck),
                        cast_spec=ctx.schema.casts[(arg_tp.tp, tp_ck)],
                        arg=arg_v)
                else:
                    raise ValueError("Cannot cast", arg_tp, tp_ck)
        case e.ShapedExprExpr(expr=subject, shape=shape):
            (subject_tp, subject_ck) = synthesize_type(ctx, subject)
            result_tp, shape_ck = check_shape_transform(
                ctx, shape, subject_tp.tp)
            if not eops.is_effect_free(shape):
                raise ValueError("Shape should be effect free", shape)
            result_card = subject_tp.mode
            result_expr = e.ShapedExprExpr(subject_ck, shape_ck)
        case e.UnionExpr(left=l, right=r):
            (l_tp, l_ck) = synthesize_type(ctx, l)
            (r_tp, r_ck) = synthesize_type(ctx, r)
            # assert l_tp.tp == r_tp.tp, "Union types must match"
            result_tp = tops.construct_tp_union(l_tp.tp, r_tp.tp)
            result_card = l_tp.mode + r_tp.mode
            result_expr = e.UnionExpr(l_ck, r_ck)
        case e.FunAppExpr(fun=fname, args=args, overloading_index=idx):
            (e_result_tp, e_ck) = func_call_checking(ctx, expr)
            result_tp = e_result_tp.tp
            result_card = e_result_tp.mode
            result_expr = e_ck
        case e.FreeObjectExpr():
            result_tp = e.NominalLinkTp(subject=e.ObjectTp({}),
                                        name=e.QualifiedName(["std", "FreeObject"]),
                                        linkprop=e.ObjectTp({}))
            result_card = e.CardOne
            result_expr = expr
        case e.ConditionalDedupExpr(expr=inner):
            (inner_tp, inner_ck) = synthesize_type(ctx, inner)
            result_tp = inner_tp.tp
            result_card = inner_tp.mode
            result_expr = e.ConditionalDedupExpr(inner_ck)
        case e.ObjectProjExpr(subject=subject, label=label):
            (subject_tp, subject_ck) = synthesize_type(ctx, subject)
            result_tp, result_card = tops.tp_project(
                ctx, subject_tp, e.StrLabel(label))
            if isinstance(result_tp, e.ComputableTp):
                comp_expr = e.WithExpr(
                    subject_ck,
                    result_tp.expr
                )
                result_expr = check_type(ctx, comp_expr, e.ResultTp(result_tp.tp, result_card))
                result_tp = result_tp.tp
            else:
                result_expr = e.ObjectProjExpr(subject_ck, label)
        case e.LinkPropProjExpr(subject=subject, linkprop=lp):
            (subject_tp, subject_ck) = synthesize_type(ctx, subject)
            result_tp, result_card = tops.tp_project(
                ctx, subject_tp, e.LinkPropLabel(lp))
            if isinstance(result_tp, e.ComputableTp):
                comp_expr = e.WithExpr(
                    subject_ck,
                    result_tp.expr
                )
                result_expr = check_type(ctx, comp_expr, e.ResultTp(result_tp.tp, result_card))
                result_tp = result_tp.tp
            else:
                result_expr = e.LinkPropProjExpr(subject_ck, lp)
        case e.BackLinkExpr(subject=subject, label=label):
            (_, subject_ck) = synthesize_type(ctx, subject)
            candidates: List[e.NamedNominalLinkTp] = []
            for (name, name_def) in mops.enumerate_all_object_type_defs(ctx):
                for (name_label, comp_tp) in name_def.val.items():
                    if name_label == label:
                        match comp_tp.tp:
                            case e.NamedNominalLinkTp(_):
                                candidates = [
                                    *candidates,
                                    e.NamedNominalLinkTp(name,
                                                 comp_tp.tp.linkprop)
                                ] 
                            case _:
                                candidates = [
                                    *candidates,
                                    e.NamedNominalLinkTp(name,
                                                 e.ObjectTp({}))
                                ]
            result_expr = e.BackLinkExpr(subject_ck, label)
            if len(candidates) == 0:
                result_tp = e.AnyTp()
            else:
                result_tp = reduce(
                    tops.construct_tp_union,  # type: ignore[arg-type]
                    candidates)
            result_card = e.CardAny
        case e.TpIntersectExpr(subject=subject, tp=intersect_tp):
            intersect_tp_name , _ = mops.resolve_raw_name_and_type_def(ctx, intersect_tp)
            (subject_tp, subject_ck) = synthesize_type(ctx, subject)
            result_expr = e.TpIntersectExpr(subject_ck, intersect_tp_name)
            if all(isinstance(t, e.NamedNominalLinkTp)
                   for t in tops.collect_tp_union(subject_tp.tp)):
                candidates = []
                for t in tops.collect_tp_union(subject_tp.tp):
                    assert isinstance(t, e.NamedNominalLinkTp)
                    # TODO: use real subtp
                    # if t.subject == e.VarTp(intersect_tp):
                    candidates = [*candidates, t]
                if len(candidates) == 0:
                    result_tp = tops.construct_tp_intersection(
                        subject_tp.tp, e.NamedNominalLinkTp(name=intersect_tp_name, linkprop=e.ObjectTp({})))
                else:
                    result_tp = reduce(
                        tops.construct_tp_union,  # type: ignore[arg-type]
                        candidates)
            else:
                result_tp = tops.construct_tp_intersection(
                    subject_tp.tp, e.NamedNominalLinkTp(name=intersect_tp_name, linkprop=e.ObjectTp({}))) #TODO: get linkprop
            result_card = e.CMMode(
                e.CardNumZero,
                subject_tp.mode.upper, 
                # subject_tp.mode.multiplicity
            )
        case e.SubqueryExpr(expr=sub_expr):
            (sub_expr_tp, sub_expr_ck) = synthesize_type(ctx, sub_expr)
            result_expr = e.SubqueryExpr(sub_expr_ck)
            result_tp = sub_expr_tp.tp
            result_card = sub_expr_tp.mode
        case e.DetachedExpr(expr=sub_expr):
            (sub_expr_tp, sub_expr_ck) = synthesize_type(ctx, sub_expr)
            result_expr = e.SubqueryExpr(sub_expr_ck)
            result_tp = sub_expr_tp.tp
            result_card = sub_expr_tp.mode
        case e.WithExpr(bound=bound_expr, next=next_expr):
            (bound_tp, bound_ck) = synthesize_type(ctx, bound_expr)
            new_ctx, body, bound_var = eops.tcctx_add_binding(
                ctx, next_expr, bound_tp)
            (next_tp, next_ck) = synthesize_type(new_ctx, body)
            result_expr = e.WithExpr(
                bound_ck, eops.abstract_over_expr(next_ck, bound_var))
            result_tp, result_card = next_tp
        case e.FilterOrderExpr(subject=subject, filter=filter, order=order):
            (subject_tp, subject_ck) = synthesize_type(ctx, subject)
            filter_ctx, filter_body, filter_bound_var = eops.tcctx_add_binding(
                ctx, filter, e.ResultTp(subject_tp.tp, e.CardOne))
            
            order_ck : Dict[str, e.BindingExpr] = {}
            for (order_label, o) in order.items():
                order_ctx, order_body, order_bound_var = eops.tcctx_add_binding(
                    ctx, o, e.ResultTp(subject_tp.tp, e.CardOne))
                (_, o_ck) = synthesize_type(order_ctx, order_body)
                order_ck = {**order_ck, order_label : eops.abstract_over_expr(o_ck, order_bound_var)}
            
            assert eops.is_effect_free(filter), "Expecting effect-free filter"
            assert all(eops.is_effect_free(o) for o in order.values()), "Expecting effect-free order"

            (_, filter_ck) = check_type_no_card(
                filter_ctx, filter_body, e.BoolTp())

            # assert tops.is_order_spec(order_tp), "Expecting order spec"

            result_expr = e.FilterOrderExpr(
                subject_ck,
                eops.abstract_over_expr(filter_ck, filter_bound_var),
                order_ck)
            result_tp = subject_tp.tp
            # pass cardinality if filter body can be determined to be true
            if filter_body == e.BoolVal(True):
                result_card = subject_tp.mode
            else:
                result_card = e.CMMode(
                    e.CardNumZero,
                    subject_tp.mode.upper
                    # subject_tp.mode.multiplicity
                )
        case e.OffsetLimitExpr(subject=subject, offset=offset, limit=limit):
            (subject_tp, subject_ck) = synthesize_type(ctx, subject)
            offset_ck = check_type(ctx, offset,
                                   e.ResultTp(e.IntTp(), e.CardAtMostOne))
            limit_ck = check_type(ctx, limit,
                                  e.ResultTp(e.IntTp(), e.CardAtMostOne))
            result_expr = e.OffsetLimitExpr(subject_ck, offset_ck, limit_ck)
            result_tp = subject_tp.tp
            if isinstance(limit_ck, e.ScalarVal):
                v = limit_ck.val
                assert isinstance(limit_ck.val, int), "Expecting int"
                if v > 1:
                    upper_card_bound = subject_tp.mode.upper
                else:
                    upper_card_bound = e.CardNumOne
            else:
                upper_card_bound = subject_tp.mode.upper



            result_card = e.CMMode(
                e.CardNumZero,
                upper_card_bound,
                # subject_tp.mode.multiplicity
            ) 
            
            # if isinstance(limit_ck, e.IntVal):
            #     lim_num = limit_ck.val
            #     result_card = e.CMMode(
            #         e.CardNumZero,
            #         e.min_cardinal(result_card.upper, 
            #                        e.CardNumInf if lim_num > 1 else 
            #                        (e.CardNumOne if lim_num == 0 else e.CardNumZero)),
            #         # e.min_cardinal(result_card.multiplicity, e.Fin(lim_num))
            #         )
        case e.InsertExpr(name=tname, new=arg):
            result_expr = insert_checking(ctx, expr)
            assert isinstance(result_expr, e.InsertExpr) and isinstance(result_expr.name, e.QualifiedName)
            result_tp = e.NamedNominalLinkTp(name=result_expr.name, linkprop=e.ObjectTp({}))
            result_card = e.CardOne
        case e.UpdateExpr(subject=subject, shape=shape_expr):
            (subject_tp, subject_ck) = synthesize_type(ctx, subject)
            (shape_ck) = update_checking(ctx, shape_expr, subject_tp.tp)
            result_expr = e.UpdateExpr(subject_ck, shape_ck)
            result_tp, result_card = subject_tp
        case e.DeleteExpr(subject=subject):
            (subject_tp, subject_ck) = synthesize_type(ctx, subject)
            assert eops.is_effect_free(subject), (
                "Expecting subject expr to be effect-free")
            result_expr = e.DeleteExpr(subject_ck)
            result_tp, result_card = subject_tp
        case e.IfElseExpr(then_branch=then_branch,
                          condition=condition,
                          else_branch=else_branch):
            (_, condition_ck) = check_type_no_card(
                ctx, condition, e.ScalarTp(e.QualifiedName(["std","bool"])))
            then_tp, then_ck = synthesize_type(ctx, then_branch)
            else_tp, else_ck = synthesize_type(ctx, else_branch)
            # TODO: should we check if they are the same?
            result_tp = tops.construct_tp_union(then_tp.tp, else_tp.tp)
            result_card = e.CMMode(
                e.min_cardinal(then_tp.mode.lower, else_tp.mode.lower),
                e.max_cardinal(then_tp.mode.upper, else_tp.mode.upper),
                # e.max_cardinal(then_tp.mode.multiplicity,
                #                else_tp.mode.multiplicity)
            )
            result_expr = e.IfElseExpr(
                    then_branch=then_ck,
                    condition=condition_ck,
                    else_branch=else_ck)
        case e.ForExpr(bound=bound, next=next):
            (bound_tp, bound_ck) = synthesize_type(ctx, bound)
            new_ctx, next_body, bound_var = eops.tcctx_add_binding(
                ctx, next, e.ResultTp(bound_tp.tp, e.CardOne))
            (next_tp, next_ck) = synthesize_type(new_ctx, next_body)
            result_expr = e.ForExpr(
                bound=bound_ck,
                next=eops.abstract_over_expr(next_ck, bound_var))
            result_tp = next_tp.tp
            result_card = next_tp.mode * bound_tp.mode
        case e.OptionalForExpr(bound=bound, next=next):
            (bound_tp, bound_ck) = synthesize_type(ctx, bound)
            if (bound_tp.mode.lower == e.CardNumZero):
                bound_card = e.CardAtMostOne 
            elif (bound_tp.mode.lower == e.CardNumOne):
                bound_card = e.CardOne
            else:
                raise ValueError("Cannot have inf as lower bound")
            new_ctx, next_body, bound_var = eops.tcctx_add_binding(
                ctx, next, e.ResultTp(bound_tp.tp, bound_card))
            (next_tp, next_ck) = synthesize_type(new_ctx, next_body)
            result_expr = e.OptionalForExpr(
                bound=bound_ck,
                next=eops.abstract_over_expr(next_ck, bound_var))
            result_tp = next_tp.tp
            result_card = next_tp.mode * e.CMMode(
                e.CardNumOne, bound_tp.mode.upper)
        case e.UnnamedTupleExpr(val=arr):
            [res_tps, cks] = zip(*[synthesize_type(ctx, v) for v in arr])
            result_expr = e.UnnamedTupleExpr(list(cks))
            [tps, cards] = zip(*res_tps)
            result_tp = e.UnnamedTupleTp(list(tps))
            result_card = reduce(operator.mul, cards, e.CardOne)
        case e.NamedTupleExpr(val=arr):
            [res_tps, cks] = zip(*[synthesize_type(ctx, v)
                                   for _, v in arr.items()])
            result_expr = e.NamedTupleExpr({k: c
                                            for k, c in zip(arr.keys(), cks)})
            [tps, cards] = zip(*res_tps)
            result_tp = e.NamedTupleTp({k: t for k, t in zip(arr.keys(), tps)})
            result_card = reduce(operator.mul, cards, e.CardOne)
        case e.ArrExpr(elems=arr):
            assert len(arr) > 0, "Empty array does not support type synthesis"
            (first_tp, first_ck) = synthesize_type(ctx, arr[0])
            rest_card: Sequence[e.CMMode]
            (rest_card, rest_cks) = zip(
                *[check_type_no_card(ctx, arr_elem, first_tp.tp)
                  for arr_elem in arr[1:]])
            # TODO: change to use unions
            result_expr = e.ArrExpr([first_ck] + list(rest_cks))
            result_tp = e.ArrTp(first_tp.tp)
            result_card = reduce(operator.mul, rest_card,
                                 first_tp.mode)  # type: ignore[arg-type]
        case e.MultiSetExpr(expr=arr):
            # if len(arr) == 0:
                # return (e.ResultTp(e.UnifiableTp(e.next_id()),
                #                    e.CardAtMostOne), expr)  # this is a hack
            assert len(arr) > 0, ("Empty multiset does not"
                                  " support type synthesis")
            (first_tp, first_ck) = synthesize_type(ctx, arr[0])
            if len(arr[1:]) == 0:
                result_expr = e.MultiSetExpr([first_ck])
                result_tp = first_tp.tp
                result_card = first_tp.mode
            else:
                (rest_res_tps, rest_cks) = zip(
                    *[synthesize_type(ctx, arr_elem)
                        for arr_elem in arr[1:]])
                rest_tps, rest_cards = zip(*rest_res_tps)
                result_expr = e.MultiSetExpr([first_ck] + list(rest_cks))
                result_tp = reduce(tops.construct_tp_union, rest_tps, first_tp.tp)
                result_card = reduce(operator.add, rest_cards,
                                     first_tp.mode)  # type: ignore[arg-type]
        case _:
            raise ValueError("Not Implemented", expr)

    # enforce singular
    # result_expr = enforce_singular(result_expr)
    # check integrity
    if isinstance(result_tp, e.ObjectTp):
        raise ValueError("Must return NominalLinkTp instead of object tp", expr, result_tp)

    return (e.ResultTp(result_tp, result_card), result_expr)

def expr_tp_is_not_synthesizable(expr: e.Expr) -> bool:
    match expr:
        case e.MultiSetExpr(expr=[]):
            return True
        case _:
            return False


def check_type_no_card(ctx: e.TcCtx, expr: e.Expr,
                       tp: e.Tp, with_assignment_cast: bool = False) -> Tuple[e.CMMode, e.Expr]:
    match expr:
        case e.MultiSetExpr(expr=[]):
            return (e.CardAtMostOne, expr)
        case _:
            expr_tp, expr_ck = synthesize_type(ctx, expr)
            default_return = (expr_tp.mode, expr_ck)
            if tops.check_is_subtype(ctx, expr_tp.tp, tp):
                return default_return
            else:
                if (expr_tp.tp, tp) in ctx.schema.casts:
                    cast_fun = ctx.schema.casts[(expr_tp.tp, tp)]
                    match cast_fun.kind:
                        case e.TpCastKind.Explicit:
                            raise ValueError("Not a sub type", expr_tp.tp, tp)
                        case e.TpCastKind.Implicit:
                            return (expr_tp.mode, 
                                    e.CheckedTypeCastExpr((expr_tp.tp, tp), cast_fun, expr_ck))
                        case e.TpCastKind.Assignment:
                            if with_assignment_cast:
                                return (expr_tp.mode, 
                                        e.CheckedTypeCastExpr((expr_tp.tp, tp), cast_fun, expr_ck))
                            else:
                                raise ValueError("Not a sub type", expr_tp.tp, tp)
                        case _:
                            raise ValueError("Not Implemented", cast_fun.kind)
                else:
                    raise ValueError("Not a sub type", expr_tp.tp, tp)



            # if tops.is_real_subtype(expr_tp.tp, tp):
            #     return (expr_tp.mode, expr_ck)
            # else:
            # raise ValueError("Type mismatch, ", expr_tp, "is not a sub"
            #                  "type of ", tp, "when checking", expr)


def check_type(ctx: e.TcCtx, expr: e.Expr, tp: e.ResultTp, with_assignment_cast: bool = False) -> e.Expr:
    synth_mode, expr_ck = check_type_no_card(ctx, expr, tp.tp, with_assignment_cast)
    tops.assert_cardinal_subtype(synth_mode, tp.mode)
    # ( "Expecting cardinality %s, got %s" % (tp.mode, synth_mode))
    return expr_ck
    

def check_type_valid(ctx: e.TcCtx | e.DBSchema, tp : e.Tp) -> e.Tp:
    """
    Check that a raw schema type is a valid type.
    Returns the checked valid type.
    """
    match tp:
        case e.UncheckedTypeName(name=name):
            resolved_name, resolved_tp = mops.resolve_raw_name_and_type_def(ctx, name)
            match resolved_tp:
                case e.ScalarTp(_):
                    return resolved_tp
                case e.ObjectTp(_):
                    return e.NamedNominalLinkTp(name=resolved_name, linkprop=e.ObjectTp({}))
                case _:
                    raise ValueError("Not Implemented", resolved_tp)
        case e.AnyTp(_):
            return tp
        case e.CompositeTp(kind=kind, tps=tps, labels=labels):
            return e.CompositeTp(kind=kind, tps=[check_type_valid(ctx, t) for t in tps], labels=labels)
        case _:
            raise ValueError("Not Implemented", tp)