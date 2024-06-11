n_electrons = int(input())
position = 1
shells = []
while n_electrons > 0:
    max_number_current_shell = 2 * position ** 2
    if n_electrons >= max_number_current_shell:
        shells.append(max_number_current_shell)
    else:
        max_number_current_shell = n_electrons
        shells.append(n_electrons)

    n_electrons -= max_number_current_shell
    position += 1

print(shells)