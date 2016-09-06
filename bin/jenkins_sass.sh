echo "Installing front end dependencies..."
npm install  # invokes jspm install (unused here)

echo "Compiling sass..."
gulp sass
