from functools import wraps
from flask import abort
from flask_login import current_user
from .models import Permission

def permission_required(permission):
	def decorator(f):
		@wraps(f)
		def decorated_function(*args, **kwargs):
			if not current_user.is_permitted(permission):
				abort(403)
			return f(*args, **kwargs)
		return decorated_function
	return decorator

def admin_only(f):
	return permission_required(Permission.ADMIN)(f)

def is_logged_in(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash('Please log in first','danger')
			return redirect('login')
	return wrap
	