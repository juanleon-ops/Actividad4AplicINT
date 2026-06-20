from flask import request
from app.extensions import db
from flask_appbuilder import BaseView, expose
from app.models.categoria import Categoria
from app.models.ingrediente import Ingrediente
from app.models.receta_ingrediente import RecetaIngrediente
from app.models.receta import Receta


class ReporteSimpleView(BaseView):

    @expose("/", methods=["GET", "POST"])
    def list(self):
        categorias = db.session.query(Categoria).all()
        categoria_seleccionada = request.form.get('cat_id')
        return self.render_template(
            "reportes.html",
            categorias=categorias,
            id_categoria=categoria_seleccionada
        )


def obtener_ingredientes(categoria_id=None):
    query = Ingrediente.query
    if categoria_id:
        query = (
            query
            .join(RecetaIngrediente, RecetaIngrediente.ingrediente_id == Ingrediente.id)
            .join(Receta, Receta.id == RecetaIngrediente.receta_id)
            .filter(Receta.categoria_id == categoria_id)
            .distinct()
        )
    return query.all()


class ReporteIngredientesView(BaseView):
    route_base = "/reporteingredientes"

    @expose("/")
    def lista(self):
        categoria_id = request.args.get("categoria_id", type=int)
        ingredientes = obtener_ingredientes(categoria_id)
        categorias = Categoria.query.all()
        return self.render_template(
            "reporte_ingredientes.html",
            ingredientes=ingredientes,
            categorias=categorias,
            categoria_seleccionada=categoria_id,
        )