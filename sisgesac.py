# ==============================================================================
# DISCIPLINA: PROGRAMAÇÃO ORIENTADA A OBJETOS
# ATIVIDADE: Cadastro de Pontos de Internet e Wi-Fi - Sistema SISGESAC
# 
# INTEGRANTES DO TRIO:
# - Arthur Moura Campos           | RA: 22602304
# - Derick Dixon Xavier Rodrigues | RA: 22602449
# - Arthur Souza Mendes           | RA: 22600960
# ==============================================================================

from abc import ABC, abstractmethod


class PontoPresenca(ABC):
    def __init__(self, id_gesac, upload, download, beam):
        self.__id_gesac = str(id_gesac)
        self.__upload = float(upload)
        self.__download = float(download)
        self.__beam = str(beam)

    @property
    def id_gesac(self):
        return self.__id_gesac

    @property
    def upload(self):
        return self.__upload

    @property
    def download(self):
        return self.__download

    @property
    def beam(self):
        return self.__beam

    def consultar(self):
        return (
            f"ID GESAC: {self.__id_gesac} | "
            f"Upload: {self.__upload} Mbps | "
            f"Download: {self.__download} Mbps | "
            f"Feixe (Beam): {self.__beam}"
        )

    @abstractmethod
    def cadastrar(self, bd):
        pass


class PontoInternet(PontoPresenca):
    def __init__(self, id_gesac, upload, download, beam):
        super().__init__(id_gesac, upload, download, beam)

    def cadastrar(self, bd):
        try:
            if self.id_gesac in bd:
                raise KeyError(f"O ID '{self.id_gesac}' já existe no cadastro de Internet.")
            bd[self.id_gesac] = self
            print(f"[SUCESSO] Ponto de Internet '{self.id_gesac}' cadastrado com êxito.")
        except Exception as erro:
            print(f"[FALHA - INTERNET] Não foi possível cadastrar '{self.id_gesac}': {erro}")


class PontoWifi(PontoPresenca):
    def __init__(self, id_gesac, upload, download, beam):
        super().__init__(id_gesac, upload, download, beam)

    def cadastrar(self, bd):
        try:
            if self.id_gesac in bd:
                raise KeyError(f"O ID '{self.id_gesac}' já consta na base do Wi-Fi.")
            if self.download < 300:
                raise ValueError(f"Download de {self.download} Mbps insuficiente. Mínimo exigido: 300 Mbps.")
            if self.upload < 30:
                raise ValueError(f"Upload de {self.upload} Mbps insuficiente. Mínimo exigido: 30 Mbps.")

            bd[self.id_gesac] = self
            print(f"[SUCESSO] Ponto Wi-Fi '{self.id_gesac}' validado e cadastrado com êxito.")
        except Exception as erro:
            print(f"[FALHA - WI-FI] Ponto '{self.id_gesac}' RECUSADO: {erro}")


if __name__ == "__main__":
    bd_internet = {}
    bd_wifi = {}

    print("=" * 65)
    print("SISTEMA SISGESAC - PROCESSO DE CADASTRO")
    print("=" * 65)

    print("\n>>> Processando Pontos de Internet Cabeada...")
    net1 = PontoInternet("GESAC-NET-01", upload=50.0, download=400.0, beam="B1-NORTE")
    net2 = PontoInternet("GESAC-NET-02", upload=20.0, download=150.0, beam="B2-SUL")
    net_duplicada = PontoInternet("GESAC-NET-01", upload=80.0, download=500.0, beam="B1-NORTE")

    net1.cadastrar(bd_internet)
    net2.cadastrar(bd_internet)
    net_duplicada.cadastrar(bd_internet)

    print("\n>>> Processando Pontos Wi-Fi...")
    wifi_ok = PontoWifi("GESAC-WIFI-01", upload=40.0, download=350.0, beam="FEIXE-A")
    wifi_down_ruim = PontoWifi("GESAC-WIFI-02", upload=50.0, download=200.0, beam="FEIXE-B")
    wifi_up_ruim = PontoWifi("GESAC-WIFI-03", upload=15.0, download=450.0, beam="FEIXE-C")

    wifi_ok.cadastrar(bd_wifi)
    wifi_down_ruim.cadastrar(bd_wifi)
    wifi_up_ruim.cadastrar(bd_wifi)

    print("\n" + "=" * 65)
    print("RELATÓRIO DE PONTOS HOMOLOGADOS E ARMAZENADOS")
    print("=" * 65)

    print("\n[BASE DE DADOS - INTERNET CABEADA]")
    if bd_internet:
        for ponto in bd_internet.values():
            print(" ->", ponto.consultar())
    else:
        print(" Nenhum ponto cadastrado.")

    print("\n[BASE DE DADOS - PONTOS WI-FI]")
    if bd_wifi:
        for ponto in bd_wifi.values():
            print(" ->", ponto.consultar())
    else:
        print(" Nenhum ponto cadastrado.")
    
    print("\n" + "=" * 65)
