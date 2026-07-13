<script setup>

import { ref,watch } from "vue"

const emit = defineEmits(["search"])

const search = ref("")

watch(search,()=>{

    emit("search",search.value)

})

</script>

<template>

<div class="search-box">

    <i class="bi bi-search"></i>

    <input

        v-model="search"

        placeholder="Search..."

    >

</div>

</template>

<style scoped>

.search-box{

    background:white;

    display:flex;

    align-items:center;

    gap:10px;

    padding:12px 18px;

    border-radius:12px;

    box-shadow:0 10px 25px rgba(0,0,0,.08);

    margin-bottom:25px;

}

.search-box input{

    border:none;

    outline:none;

    width:100%;

    font-size:15px;

}

.search-box i{

    color:#6366f1;

    font-size:18px;

}

</style>