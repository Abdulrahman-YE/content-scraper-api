#!/bin/bash

# Path to exported JSON file
JSON_FILE="./trending_searches_IN.json"

# Output folder
OUTPUT_DIR="trending_articles"
mkdir -p "$OUTPUT_DIR"

# Loop through each item in the JSON file
jq -c '.[]' "$JSON_FILE" | while read -r item; do
  # Extract keyword and loop through its news articles
  keyword=$(echo "$item" | jq -r '.title')
  safe_keyword=$(echo "$keyword" | tr ' ' '_' | tr -cd '[:alnum:]_-')
  folder="$OUTPUT_DIR/$safe_keyword"
  mkdir -p "$folder"

  echo "$item" | jq -c '.raw_data.news[]' | while read -r article; do
    url=$(echo "$article" | jq -r '.url')

    # Skip if URL is empty
    if [ -z "$url" ]; then continue; fi

    # Hash the URL for unique file naming
    hash=$(echo -n "$url" | md5sum | awk '{print $1}')
    filename="$folder/${hash}.json"

    echo "Fetching article for: $keyword -> $url"

    curl -s -X POST http://localhost:8000/fetch-article \
      -H "Content-Type: application/json" \
      -d "{\"url\": \"$url\"}" \
      -o "$filename"

    # Pretty-print with jq
    if command -v jq &> /dev/null; then
      jq . "$filename" > "$filename.pretty" && mv "$filename.pretty" "$filename"
    fi
  done
done

echo "✅ All articles fetched and grouped in '$OUTPUT_DIR'"
