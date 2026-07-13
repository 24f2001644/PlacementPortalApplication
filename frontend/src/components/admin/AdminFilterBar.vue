<script setup>

import { ref } from "vue"

const search = ref("")
const status = ref("")

const emit = defineEmits([

    "filter"

])

function applyFilter(){

    emit(

        "filter",

        {

            search:search.value,

            status:status.value

        }

    )

}

</script>

<template>

<div class="filter-bar">

    <input
        class="form-control"
        placeholder="Search..."
        v-model="search"
    >

    <select
        class="form-select"
        v-model="status"
    >

        <option value="">

            All Status

        </option>

        <option>

            Approved

        </option>

        <option>

            Pending

        </option>

        <option>

            Rejected

        </option>

    </select>

    <button
        class="btn btn-primary"
        @click="applyFilter"
    >
        Filter
    </button>

</div>

</template>

<style scoped>

.filter-bar{

display:flex;

gap:15px;

background:white;

padding:18px;

border-radius:16px;

box-shadow:0 10px 25px rgba(0,0,0,.05);

margin-bottom:25px;

}

</style>