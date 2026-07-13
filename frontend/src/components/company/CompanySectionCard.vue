<template>

<div class="section-card">

    <div
        v-if="title"
        class="card-header"
    >

        <h5>

            {{ title }}

        </h5>

        <slot name="actions"></slot>

    </div>

    <div class="card-body">

        <slot />

    </div>

</div>

</template>

<script setup>

defineProps({

    title:String

})

</script>

<style scoped>

.section-card{

background:white;

border-radius:18px;

box-shadow:0 8px 24px rgba(0,0,0,.05);

overflow:hidden;

margin-bottom:25px;

}

.card-header{

display:flex;

justify-content:space-between;

align-items:center;

padding:20px 25px;

border-bottom:1px solid #E2E8F0;

}

.card-header h5{

margin:0;

font-size:18px;

font-weight:700;

color:#0F172A;

}

.card-body{

padding:25px;

}

</style>