import random
import string

def generate_random_string(k):
  return "".join(random.choices(
    string.ascii_uppercase + string.ascii_lowercase +
    string.digits, k=k)
  )

def allowed_file(filename, allowed_extensions):
  return '.' in filename and \
    get_extension(filename) \
    in allowed_extensions

def get_extension(filename):
  return filename.rsplit('.', 1)[1].lower()