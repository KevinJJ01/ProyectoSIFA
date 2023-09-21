from flask import render_template, flash,redirect
from flask_login import login_required
from app.usuario import usuario
import app
import os
from .forms import NewUsuaForm, EditUsuaForm

@usuario.route('/createUsuario',methods=['GET','POST'])
@login_required
def crear():
    p = app.models.Cliente()
    form = NewUsuaForm()
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.add(p)
        app.db.session.commit()
        return redirect('/usuario/listarU')
    return render_template('new.html',
                           form=form)


@usuario.route('/listarC')
@login_required
def listar():
     ## seleccionar los profuctos
    usuario = app.models.Usuario.query.all()
    return render_template("listC.html", 
                            usuario = usuario)  
 
@usuario.route('/editar/<usuario_id>',methods=['GET','POST'])
@login_required
def editar (idUsuario):
    p = app.models.usuario.query.get(idUsuario)
    form = EditUsuaForm(obj = p)
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.commit()
        flash('usuario actualizado')
        return redirect('/usuario/listarC')
    return render_template('new.html',
                           form=form)

@usuario.route('/eliminar/<usuario_id>')
@login_required
def eliminar (usuario_id):
    p = app.models.usuario.query.get(usuario_id)
    app.db.session.delete(p)
    app.db.session.commit()
    flash('usuario eliminado')
    return redirect('/usuario/listarC')


