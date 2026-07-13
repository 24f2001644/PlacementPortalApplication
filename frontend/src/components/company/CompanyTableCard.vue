<template>

<div class="table-card">

    <div class="table-header">

        <h5>

            {{ title }}

        </h5>

        <slot name="actions"></slot>

    </div>

    <div class="table-responsive">

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

.table-card{

background:white;

border-radius:18px;

box-shadow:0 8px 24px rgba(0,0,0,.05);

overflow:hidden;

}

.table-header{

display:flex;

justify-content:space-between;

align-items:center;

padding:20px 25px;

border-bottom:1px solid #E2E8F0;

}

.table-header h5{

margin:0;

font-size:18px;

font-weight:700;

color:#0F172A;

}

.table-responsive{

padding:20px;

}

.table{

margin-bottom:0;

}

.table thead th{

background:#F8FAFC;

color:#334155;

font-weight:700;

border-bottom:none;

padding:14px;

}

.table tbody td{

padding:14px;

vertical-align:middle;

}

.table tbody tr{

transition:.2s;

}

.table tbody tr:hover{

background:#F8FAFC;

}

</style>