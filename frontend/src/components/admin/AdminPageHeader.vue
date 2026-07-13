<script setup>

defineProps({

    title:String,

    subtitle:String

})

</script>

<template>

<div class="page-header">

    <div>

        <h2>{{ title }}</h2>

        <p>{{ subtitle }}</p>

    </div>

</div>

</template>

<style scoped>

.page-header{

    display:flex;

    justify-content:space-between;

    align-items:center;

    margin-bottom:25px;

}

.page-header h2{

    font-weight:700;

    color:#1e293b;

}

.page-header p{

    color:#64748b;

    margin-top:5px;

}

</style>