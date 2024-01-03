param(
    [string]$appName
)

$npxCommand = "npx create-vite $appName --template $framework"
Invoke-Expression -Command $npxCommand

Set-Location -Path $appName

# Install Tailwind CSS
$installTailwindCommand = "npm install tailwindcss@latest postcss@latest autoprefixer@latest"
Invoke-Expression -Command $installTailwindCommand

# Initialize Tailwind CSS
$initTailwindCommand = "npx tailwindcss init -p"
Invoke-Expression -Command $initTailwindCommand

npm install
npm run dev