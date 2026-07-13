<script setup>

defineProps({

title:String

})

</script>

<template>

<div class="section-card">

    <div class="section-header">

        <h5>

            {{ title }}

        </h5>

    </div>

    <div class="section-body">

        <slot />

    </div>

</div>

</template>

<style scoped>

.section-card{

background:white;

border-radius:18px;

overflow:hidden;

box-shadow:0 12px 35px rgba(0,0,0,.08);

}

.section-header{

padding:18px 25px;

border-bottom:1px solid #e2e8f0;

font-weight:600;

}

.section-body{

padding:25px;

}

</style>