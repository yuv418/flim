from app import app

import os

if __name__=='__main__':
	app.run(debug=os.getenv("FLASK_DEBUG", False), host=os.getenv("FLIM_HOST", "0.0.0.0"))
