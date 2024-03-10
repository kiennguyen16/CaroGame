from XO import XO
game = XO()
game.print_board()
print("Người chơi X chọn ô")
while True:
    row = int(input("Chọn hàng từ 0 đến 2: "))
    col = int(input("Chọn cột từ 0 đến 2: "))
    game.make_move(row, col)
    game.print_board()
    if game.checkFull():
        print("Hòa")
        break
    elif game.check_winner():
        print(f"Chúc mừng người chiến thắng là người chơi: {game.check_winner()}")
        break

