<template>
  <div>
    <input v-model="query" @input="buscarOperadoras" placeholder="Buscar operadoras..." />
    <ul>
      <li v-for="operadora in resultados" :key="operadora.nome">
        {{ operadora.nome }} - {{ operadora.servico }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      query: '',
      resultados: [],
    };
  },
  methods: {
    buscarOperadoras() {
      if (this.query.trim() === '') {
        this.resultados = [];
        return;
      }

      axios
        .get(`http://127.0.0.1:5000/api/busca`, {
          params: { query: this.query },
        })
        .then((response) => {
          this.resultados = response.data;
        })
        .catch((error) => {
          console.error('Erro ao buscar operadoras:', error);
        });
    },
  },
};
</script>
