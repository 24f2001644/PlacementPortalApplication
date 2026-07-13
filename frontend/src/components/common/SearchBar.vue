<template>

<div class="input-group mb-3">

    <span class="input-group-text">

        <i class="bi bi-search"></i>

    </span>

    <input

        class="form-control"

        type="text"

        placeholder="Search..."

        v-model="search"

        @input="emitSearch"

    >

</div>

</template>

<script setup>

import { ref } from "vue";

const emit = defineEmits(["search"]);

const search = ref("");

function emitSearch(){

    emit(

        "search",

        search.value

    );

}

</script>