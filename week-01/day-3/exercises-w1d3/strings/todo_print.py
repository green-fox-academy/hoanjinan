# Add "My todo:" to the beginning of the todoText
# Add " - Download games" to the end of the todoText
# Add " - Diablo" to the end of the todoText but with indention

# Expected outpt:

# My todo:
#  - Buy milk
#  - Download games
#      - Diablo

todoText = " - Buy milk\n"
do = " - My todo:\n"
download = " - Download games\n"
game = "\t - Diablo"

todoText = do + todoText + download + game

print(todoText)