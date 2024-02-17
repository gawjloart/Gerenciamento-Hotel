<template>
  <div>
    <h2>Adicionar Quarto</h2>
    <form @submit.prevent="adicionarQuarto">
      <input type="text" v-model="estado" placeholder="Estado">
      <button type="submit">Adicionar</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      estado: ''
    }
  },
  methods: {
    adicionarQuarto() {
      axios.post('/quartos', { estado: this.estado })
        .then(response => {
          alert(response.data.message)
          this.estado = ''
          this.$emit('quartoAdicionado')
        })
        .catch(error => {
          console.error('Erro ao adicionar quarto:', error)
        })
    }
  }
}
</script>
