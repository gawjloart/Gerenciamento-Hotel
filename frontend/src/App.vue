<template>
  <div id="app">
    <h1>Hotel</h1>
    <Quartos />
    <NovoQuarto />
  </div>
</template>

<script>
import Quartos from './components/Quartos.vue'
import NovoQuarto from './components/NovoQuarto.vue'

export default {
  components: {
    Quartos,
    NovoQuarto
  }
}
</script>
