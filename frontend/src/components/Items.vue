<template>
  <div id="itemtable" class="itemtable" >
    <h1>Items</h1>

    <form @submit.prevent="sendData" >
      <select v-model="selected_column" id="select1">
        <option selected disabled>Выбор колонки</option>
        <option value="name">Имя</option>
        <option value="count">Количество</option>
        <option value="distance">Расстояние</option>
      </select>

      <select v-model="selected_clause" id="select2">
        <option selected disabled >Выбор условия</option>
        <option value="equals">равно</option>
        <option value="contains">содержит</option>
        <option>больше</option>
        <option>меньше</option>
      </select>


      <input v-model="sort_value" size="25" placeholder="значение для сортировки" id="input">


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
import axios from 'axios';
import Vue from "vue";


export default {
  data() {
    return {
      items: [],
      sort_value: null,
      selected_clause: null,
      selected_column: null,
      infoId: null,
      sendInfo: null,
      articleId: null
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

    sendData(){
      const path = 'http://localhost:8000/data/';
      const article = { sort_value: this.sort_value, selected_clause: this.selected_clause, selected_column: this.selected_column };
      axios.post(path, article);
    }


  },
  created() {
    this.getItems();
  },
};

</script>
