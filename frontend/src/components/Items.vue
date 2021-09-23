<template xmlns="http://www.w3.org/1999/html">
  <div id="itemtable" class="itemtable" >
    <h1>Items</h1>

    <form @submit.prevent="sendData" novalidate >

      <select v-model="dataform.selected_column" id="select1">
        <option selected disabled>Выбор колонки</option>
        <option value="date">Дата</option>
        <option value="name">Имя</option>
        <option value="count">Количество</option>
        <option value="distance">Расстояние</option>
      </select>

      <div v-if="dataform.selected_column === 'count' || dataform.selected_column === 'distance' || dataform.selected_column === 'date'">

        <select v-model="dataform.selected_clause" id="select2.1">
        <option selected disabled >Выбор условия</option>
        <option value="equals">равно</option>
        <option value="more">больше</option>
        <option value="less">меньше</option>
        </select>
      </div>

      <div v-else>
        <select v-model="dataform.selected_clause" id="select2">
        <option selected disabled >Выбор условия</option>
        <option value="equals">равно</option>
        <option value="contains">содержит</option>
        <option value="more">больше</option>
        <option value="less">меньше</option>
      </select>
      </div>



      <input v-model="dataform.sort_value" size="25" placeholder="значение для сортировки" id="input">

      <button @click="sendData" type="submit">Отфильтровать</button>

    </form>


    <table>
      <thead>
        <tr>
          <th>Имя</th>
          <th>Дата</th>
          <th>Количество</th>
          <th>Расстояние</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in items" :key="index">
          <td>{{ item.name }}</td>
          <td>{{ item.date }}</td>
          <td>{{ item.count }}</td>
          <td>{{ item.distance }}</td>
        </tr>
      </tbody>
    </table>

  </div>
</template>

<script>
import axios from 'axios'
import { required } from 'vuelidate/lib/validators';

export default {
  data() {
    return {
      items: [],
      dataform: {
        sort_value: null,
        selected_clause: null,
        selected_column: null,
        sendInfo: null,
        errors: [],
        submitStatus: null
      }

    };
  },

  methods: {
    getItems() {
      const path = 'http://localhost:8000/items/';
      axios
          .get(path)
          .then(res => (this.items = res.data))
          .catch((error) => {
            console.error(error);
          });

    },
    updateItems() {
      const path = 'http://localhost:8000/data/';
      axios
          .get(path)
          .then(res => (this.items = res.data))
          .catch((error) => {
            console.error(error);
          });
      this.reloadComponentForce()
    },
    reloadComponentForce() {
      this.$forceUpdate();
    },


    sendData(){
      const path = 'http://localhost:8000/data/';
      const article = { sort_value: this.dataform.sort_value, selected_clause: this.dataform.selected_clause, selected_column: this.dataform.selected_column };
      axios.post(path, article);
      this.updateItems();

    },

  },
  created() {
    this.getItems();

  },
};

</script>
