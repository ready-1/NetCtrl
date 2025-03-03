from werkzeug.security import generate_password_hash, check_password_hash

# The hash from our database
db_hash = 'pbkdf2:sha256:150000$lZ1jHAEq$5088d4c193abd15a5d71c95c494e4b7de91e8785bc19df1913b382aeb41b49b6'

# Check if the hash matches 'changeme'
is_valid = check_password_hash(db_hash, 'changeme')
print(f"Is 'changeme' valid for the stored hash? {is_valid}")

# Generate a new hash for 'changeme'
new_hash = generate_password_hash('changeme')
print(f"New hash for 'changeme': {new_hash}")
print(f"Verification: {check_password_hash(new_hash, 'changeme')}")

# Try an alternative password 'admin123'
alt_hash = generate_password_hash('admin123')
print(f"Hash for 'admin123': {alt_hash}")
print(f"Is 'admin123' valid for the stored hash? {check_password_hash(db_hash, 'admin123')}")
