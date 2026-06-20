from .categoria_view import CategoriaView
from .ingrediente_view import IngredienteView
from app.views.reportes import ReporteIngredientesView
appbuilder.add_view(
    ReporteIngredientesView,
    "Reporte de Ingredientes",
    icon="fa-lemon-o",
    category="Reportes")
