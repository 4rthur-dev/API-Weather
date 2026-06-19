# ⛅ Previsão do Tempo

Aplicação desktop desenvolvida em **Python** com **PyQt5** que permite consultar as informações climáticas de qualquer cidade em tempo real, utilizando a [OpenWeatherMap API](https://openweathermap.org/api).

## 📋 Funcionalidades

- 🔎 Busca de clima por nome da cidade
- 🌡️ Temperatura atual, mínima e máxima
- 💧 Umidade do ar
- 🌬️ Velocidade do vento
- ☁️ Descrição climática (em português)
- 🧹 Botão para limpar os campos e iniciar uma nova busca
- ✅ Validação de entrada (impede a digitação de números no campo de busca)

## 🖥️ Tecnologias utilizadas

- [Python 3](https://www.python.org/)
- [PyQt5](https://pypi.org/project/PyQt5/) — interface gráfica
- [Requests](https://pypi.org/project/requests/) — requisições HTTP
- [OpenWeatherMap API](https://openweathermap.org/api) — dados climáticos

## 📦 Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Instale as dependências:
   ```bash
   pip install PyQt5 requests
   ```

3. Configure sua chave de API:

   Crie uma conta gratuita em [OpenWeatherMap](https://openweathermap.org/api) e gere sua chave (API Key). Em seguida, substitua o valor da variável `key` no código pelo seu próprio token:

   ```python
   key = "SUA_CHAVE_AQUI"
   ```

   > ⚠️ **Importante:** evite subir sua chave de API real para repositórios públicos. O ideal é utilizar variáveis de ambiente ou um arquivo `.env` para mantê-la segura.

## ▶️ Como executar

Com as dependências instaladas e a chave de API configurada, execute:

```bash
python app.py
```

## 🚀 Como usar

1. Digite o nome da cidade desejada no campo de busca.
2. Clique em **"Ver Clima"** para consultar as informações.
3. Os dados de temperatura, umidade, vento e descrição serão exibidos na tela.
4. Use o botão **"Limpar"** para resetar os campos e fazer uma nova busca.

## 📸 Preview

> Adicione aqui um screenshot da aplicação em funcionamento.

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma *issue* ou enviar um *pull request* com melhorias, correções de bugs ou novas funcionalidades.

## 📄 Licença

Este projeto está disponível sob a licença MIT. Sinta-se livre para utilizá-lo e modificá-lo.
