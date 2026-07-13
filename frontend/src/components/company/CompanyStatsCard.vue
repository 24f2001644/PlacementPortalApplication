<template>

<div

    class="stats-card"

    :class="color"

>

    <div>

        <small>

            {{ title }}

        </small>

        <h3>

            {{ value }}

        </h3>

    </div>

    <div class="icon">

        <i :class="icon"></i>

    </div>

</div>

</template>

<script setup>

defineProps({

    title:String,

    value:[String,Number],

    icon:String,

    color:String

})

</script>

<style scoped>

.stats-card{

background:white;

border-radius:18px;

padding:22px;

display:flex;

justify-content:space-between;

align-items:center;

box-shadow:0 8px 24px rgba(0,0,0,.05);

transition:.25s;

cursor:pointer;

}

.stats-card:hover{

transform:translateY(-4px);

}

.stats-card small{

color:#64748B;

font-size:14px;

}

.stats-card h3{

margin-top:10px;

font-size:28px;

font-weight:700;

color:#0F172A;

}

.icon{

width:60px;

height:60px;

border-radius:16px;

display:flex;

align-items:center;

justify-content:center;

font-size:28px;

color:white;

}

.primary .icon{

background:#2563EB;

}

.success .icon{

background:#16A34A;

}

.warning .icon{

background:#F59E0B;

}

.danger .icon{

background:#DC2626;

}

.info .icon{

background:#0891B2;

}

.secondary .icon{

background:#7C3AED;

}

</style>