import re


# traduz 123.456.789-10 para 12345678910
def _translate(cpf):
    return "".join(re.findall(r"\d", cpf))


def _exceptions(cpf):
    """Se o número de CPF estiver dentro das exceções é inválido"""
    if len(cpf) != 11:
        return True
    else:
        cpf_str = "".join(str(x) for x in cpf)
        if cpf_str in (
            "00000000000",
            "11111111111",
            "22222222222",
            "33333333333",
            "44444444444",
            "55555555555",
            "66666666666",
            "77777777777",
            "88888888888",
            "99999999999",
        ):
            return True
    return False


def _gen(cpf):
    """Gera o próximo dígito do número de CPF"""
    res = []
    for i, a in enumerate(cpf):
        b = len(cpf) + 1 - i
        res.append(b * a)

    res = sum(res) % 11

    if res > 1:
        return 11 - res
    else:
        return 0


class CPF:
    _gen = staticmethod(_gen)
    _translate = staticmethod(_translate)

    def __init__(self, cpf) -> None:
        """O argumento cpf pode ser uma string nas formas:

        12345678910
        123.456.789-10

        ou uma lista ou tuple
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 0]
        (1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 0)

        """

        if isinstance(cpf, str):
            if not cpf.isdigit():
                cpf = self._translate(cpf)

        self.cpf: list[int] = [int(x) for x in cpf]

    def __getitem__(self, index):
        """Retorna o dígito em index como string"""

        return self.cpf[index]

    def __repr__(self) -> str:
        """Retorna uma representação 'real', ou seja:

        eval(repr(cpf)) == cpf

        """

        return "CPF('%s')" % "".join(str(x) for x in self.cpf)

    def __eq__(self, other) -> bool:
        """Provê teste de igualdade para números de CPF"""

        return isinstance(other, CPF) and self.cpf == other.cpf

    def __str__(self) -> str:
        """Retorna uma representação do CPF na forma:

        123.456.789-10

        """

        d = iter("..-")
        s: list[str] = [str(x) + (next(d) if i + 1 in range(3, 12, 3) else "") for (i, x) in enumerate(self.cpf)]
        r = "".join(s)
        return r

    def is_valid(self) -> bool:
        """Valida o número de cpf"""

        if _exceptions(self.cpf):
            return False

        s = self.cpf[:9]
        s.append(self._gen(s))
        s.append(self._gen(s))
        return s == self.cpf[:]
