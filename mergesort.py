import os
import tempfile

class File:
    def __init__(self, name):
        self.name = name

    def len(self):
        counter = 0
        with open(self.name, 'r') as file_:
            for _ in file_:
                counter += 1
        return counter
    
    def deleteln(self, line: int):
        with open(self.name, 'r') as file_read, \
                open('temp.txt', 'w') as file_write:
            contador = 1
            for linha in file_read:
                if contador != line:
                    file_write.write(linha)
                contador += 1

        os.remove(self.name)
        os.rename('temp.txt', self.name)

    def line(self, number: int):
        counter = 0
        with open(self.name, 'r') as file_:
            for line in file_:
                if counter == number:
                    return line
                counter += 1
        raise IndexError("Linha fora dos limites do arquivo.")

    def rangeln(self, begin: int, end: int = None):
        counter = 0
        temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w+')

        with open(self.name, 'r') as file_:
            for line in file_:
                if counter >= begin:
                    if end is not None and counter == end:
                        break
                    temp_file.write(line)
                counter += 1

        temp_file.seek(0)  # Volta o cursor para o início para futuras leituras
        temp_file.close()  # Fecha o arquivo temporário para que possa ser acessado
        return temp_file.name

    def delete(self):
        os.remove(self.name)


class MSE:
    def __init__(self, unordened_file: File, filter = float):
        self.unordened_file = unordened_file
        self.filter = filter

    def mergeSort(self, file: File):
        # Se o arquivo tem uma linha ou está vazio, já está "ordenado"
        if file.len() <= 1:
            return file

        mid = file.len() // 2

        # Divide o arquivo em duas partes
        left_half_name = file.rangeln(0, mid)
        right_half_name = file.rangeln(mid)

        # Chamada recursiva do mergeSort
        left_sorted = self.mergeSort(File(left_half_name))
        right_sorted = self.mergeSort(File(right_half_name))

        return self.merge(left_sorted, right_sorted)

    def merge(self, left: File, right: File):
        result = tempfile.NamedTemporaryFile(delete=False, mode='w+')

        i = j = 0

        # Mescla os dois arquivos até que todos os elementos sejam processados
        while i < left.len() and j < right.len():
            left_line = left.line(i)
            right_line = right.line(j)

            if self.filter(left_line.rstrip()) < self.filter(right_line.rstrip()):
                result.write(left_line)
                i += 1
            else:
                result.write(right_line)
                j += 1

        # Adiciona as linhas restantes do arquivo esquerdo, se houver
        for line in range(i, left.len()):
            result.write(left.line(line))

        # Adiciona as linhas restantes do arquivo direito, se houver
        for line in range(j, right.len()):
            result.write(right.line(line))

        result.seek(0)  # Volta o cursor para o início para futuras leituras
        result.close()  # Fecha o arquivo temporário para que possa ser acessado

        return File(result.name)

    def sort(self):
        sorted_file = self.mergeSort(self.unordened_file)
        print(f"Arquivo ordenado gerado: {sorted_file.name}")
        return sorted_file.name
