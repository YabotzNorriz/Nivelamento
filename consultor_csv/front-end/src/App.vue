<script setup>
import Lista from './components/Lista.vue';
</script>

<template>

  <div class="wrapper">
    <Lista />
  </div>

  <footer>
    <p>Feito por: João Pedro Andrade Paes Pimentel Barbosa</p>
  </footer>

</template>

<style>
body {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  margin: 0;
}

#app {
  display: flex;
  flex-direction: column;
  flex-grow: 1;
}

footer {
  background-color: #fff;
  padding: 10px 0;
  text-align: center;
  align-items: center;
  border-top: 1px solid #ccc;
  margin-top: auto;
}
</style>
