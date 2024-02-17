<template>
  <div>
    <h2>Quartos</h2>
    <ul>
      <li v-for="quarto in quartos" :key="quarto[0]">
        ID: {{ quarto[0] }},
        Estado: {{ quarto[1] }},
        Cliente: {{ quarto[2] }},
        Email: {{ quarto[3] || 'N/A' }},
        Check-in: {{ quarto[4] || 'N/A' }},
        Check-out: {{ quarto[5] || 'N/A' }},
        Valor: {{ quarto[6] || 'N/A' }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      quartos: []
    }
  },
  mounted() {
    this.fetchQuartos()
  },
  methods: {
    fetchQuartos() {
      axios.get('/quartos')
        .then(response => {
          this.quartos = response.data
        })
        .catch(error => {
          console.error('Erro ao buscar quartos:', error)
        })
    }
  }
}
</script>
