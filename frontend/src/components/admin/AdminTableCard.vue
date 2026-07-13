<script setup>

defineProps({

    title:String

})

</script>

<template>

<div class="table-card">

    <div class="table-header">

        <h4>{{ title }}</h4>
    </div>

    <div class="table-body">

        <slot/>

    </div>

</div>

</template>

<style scoped>

.table-card{

    background:white;

    border-radius:16px;

    box-shadow:0 15px 35px rgba(0,0,0,.08);

    overflow:hidden;

}

.table-header{

    padding:18px 25px;

    background:#f8fafc;

    border-bottom:1px solid #e2e8f0;

}

.table-header h4{

    margin:0;

    font-weight:600;

}

.table-body{

    padding:20px;

}

</style>