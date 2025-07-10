from flask import Blueprint, redirect, session
cerrar = Blueprint('cerrar', __name__)

@cerrar.route('/logout')
def logout():
    session.clear()
    return redirect('/iniciar_sesion')
