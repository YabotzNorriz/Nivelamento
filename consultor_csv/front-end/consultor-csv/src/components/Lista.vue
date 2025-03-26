<template>
  <div class="app-container">
    <div class="content">
      <h1>Busca de Operadoras</h1>
      <input type="text" v-model="query" @input="buscarOperadoras" placeholder="Digite sua busca..." />
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
            <th>Data Registro</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="operadora in resultados" :key="operadora.Registro_ANS">
            <td>{{ operadora.Nome_Fantasia || "Não informado" }}</td>
            <td>{{ operadora.Razao_Social || "Não informado" }} </td>
            <td>{{ operadora.CNPJ }}</td>
            <td>{{ operadora.Logradouro }}, {{ operadora.Numero }}, {{ operadora.Complemento }} - {{ operadora.Bairro }}
            </td>
            <td>{{ operadora.Cidade }} / {{ operadora.UF }}</td>
            <td v-if="operadora.Telefone != ''">({{ operadora.DDD }}) {{ operadora.Telefone }} / {{ operadora.Fax ||
              "Não informado" }}
            </td>
            <td v-else>{{ "Não informado" }}</td>
            <td>{{ operadora.Endereco_eletronico || "Não informado" }}</td>
            <td>{{ operadora.Data_Registro_ANS }}</td>
          </tr>
        </tbody>
      </table>
      <p v-else class="sem-resultados">Nenhum resultado encontrado.</p>
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
  align-items: center;
  min-height: 100vh;
  background-color: #eef2f5;
}

.content {
  margin: 10px;
  width: 100%;
  background: #fff;
  padding: 20px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
  border-radius: 6px;
}

h1 {
  text-align: center;
  margin-top: 0;
}

input {
  display: flex;
  width: 90%;
  margin: 20px auto;
  padding: 10px;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  text-align: left;
}


table {
  width: 100%;
  border-collapse: collapse;
  table-layout: auto;
  font-family: Arial, sans-serif;
}

thead th,
tbody td {
  padding: 10px;
  border: 1px solid #ddd;
  text-align: left;
  word-wrap: break-word;
}

tbody tr:nth-child(even) {
  background-color: #fafafa;
}

.sem-resultados {
  text-align: center;
  color: #555;
  font-style: italic;
  margin-top: 20px;
}
</style>