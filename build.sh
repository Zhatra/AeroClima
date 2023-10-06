#comandos mandados a ejecutar en vercel para el correcto deploy del proyecto

pip install -r requirements.txt 
python3 manage.py collectstatic --no-input
