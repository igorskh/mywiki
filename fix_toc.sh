if [[ "$OSTYPE" == "darwin"* ]]; then
    sed -E -i '' 's/(.+)\.html/\1\//g' public/index.html
else
    sed -E -i 's/(.+)\.html/\1\//g' public/index.html
fi