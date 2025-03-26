<template>
  <div class="app-container">
    <div class="content">
      <h1>Busca de Operadoras</h1>
      <input type="text" v-model="query" @input="buscarOperadoras" placeholder="Digite sua busca..." />
      <div class="table">
        <table v-if="resultados.length">
          <thead>
            <tr>
              <th>Nome Fantasia</th>
              <th>Razão Social</th>
              <th>CNPJ</th>
              <th>Endereço</th>
              <th>Cidade / UF</th>
              <th>Telefone / Fax</th>
              <th>Endereço Eletrônico</th>
              <th>Representante / Cargo</th>
              <th>Região</th>
              <th>Data Registro</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="operadora in resultados" :key="operadora.Registro_ANS">
              <td>{{ operadora.Nome_Fantasia || "Não informado" }}</td>
              <td>{{ operadora.Razao_Social || "Não informado" }} </td>
              <td>{{ operadora.CNPJ }}</td>
              <td>{{ operadora.Logradouro }}, {{ operadora.Numero }}, {{ operadora.Complemento }} - {{ operadora.Bairro
              }}
              </td>
              <td>{{ operadora.Cidade }} / {{ operadora.UF }}</td>
              <td v-if="operadora.Telefone != ''">({{ operadora.DDD || "Não informado" }}) {{ operadora.Telefone }} / {{
                operadora.Fax ||
                "Não informado" }}
              </td>
              <td v-else>{{ "Não informado" }}</td>
              <td>{{ operadora.Endereco_eletronico || "Não informado" }}</td>
              <td>{{ operadora.Representante || "Não informado" }} / {{ operadora.Cargo_Representante }}</td>
              <td>{{ operadora.Regiao_de_Comercializacao || "Não informado" }}</td>
              <td>{{ operadora.Data_Registro_ANS }}</td>
            </tr>
          </tbody>
        </table>
        <p v-else class="sem-resultados">Nenhum resultado encontrado.</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "OperadoraBusca",
  data() {
    return {
      query: "",
      resultados: [],
    };
  },
  methods: {
    buscarOperadoras() {
      if (this.query.trim() === "") {
        this.resultados = [];
        return;
      }

      axios
        .get("http://127.0.0.1:5000/api/busca", {
          params: { query: this.query },
        })
        .then((response) => {
          this.resultados = response.data;
        })
        .catch((error) => {
          console.error("Erro ao buscar operadoras:", error);
          this.resultados = [];
        });
    },
  },
};
</script>

<style scoped>
.app-container {
  display: flex;
  justify-content: center;
  padding: 20px;
}

.content {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.table-box {
  max-height: 400px;
  max-width: 100%;
  overflow: auto;
  margin-top: 20px;
}

h1 {
  text-align: center;
}

input {
  width: 50%;
  padding: 8px;
  margin-top: 10px;
  margin-bottom: 30px;
  text-align: left;
}

table {
  width: 100%;
  border-collapse: collapse;
  border: 1px solid #000000;
}

td {
  border: 1px solid #000000;
  padding: 8px;
}

th {
  border: 1px solid #000000;
  padding: 8px;
  background-color: #ccc;
}

tbody tr:nth-child(even) {
  background-color: #ffffff;
}

tbody tr:nth-child(odd) {
  background-color: #fff9f9;
}

.sem-resultados {
  text-align: center;
  padding: 20px;
  font-style: italic;
}
</style>