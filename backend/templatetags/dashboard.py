from django import template
from ..models import *

register = template.Library()


@register.simple_tag
def totales():
    ingresos = 0.0
    gastos = 0.0
    costos = 0.0
    for a in Account.objects.filter(type=AccountType.INGRESO):
        ingresos += a.total_credit()
    for a in Account.objects.filter(type=AccountType.GASTO):
        gastos += a.total_debit()
    for a in Account.objects.filter(type=AccountType.COSTO):
        costos += a.total_debit()

    utilidad = round(ingresos - (gastos + costos), 2)
    return {
        'INGRESOS': ingresos,
        'GASTOS': gastos,
        'COSTOS': costos,
        'UTILIDAD': utilidad,
        'IMPUESTO': round(utilidad * 0.3, 2),
    }
