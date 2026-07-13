<script setup>

defineProps({

title:String,

message:String

})

</script>

<template>

<div class="empty">

<i class="bi bi-folder2-open"></i>

<h4>

{{ title }}

</h4>

<p>

{{ message }}

</p>

</div>

</template>

<style scoped>

.empty{

padding:70px;

text-align:center;

color:#94A3B8;

}

.empty i{

font-size:65px;

margin-bottom:20px;

color:#CBD5E1;

}

.empty h4{

color:#475569;

margin-bottom:12px;

}

</style>