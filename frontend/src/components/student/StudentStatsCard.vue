<template>
    <div class="stats-card">

        <div class="icon-box">
            <i :class="icon"></i>
        </div>

        <div class="content">
            <h2>{{ value ?? 0 }}</h2>
            <p>{{ title }}</p>
        </div>

    </div>
</template>

<script setup>

defineProps({

    title: {
        type: String,
        default: ""
    },

    value: {
        type: [Number, String],
        default: 0
    },

    icon: {
        type: String,
        default: "bi bi-bar-chart"
    }

})

</script>

<style scoped>

.stats-card{

    background:#fff;

    border-radius:18px;

    padding:22px;

    display:flex;

    align-items:center;

    gap:18px;

    box-shadow:0 8px 24px rgba(15,23,42,.08);

    transition:.25s;

    height:100%;

}

.stats-card:hover{

    transform:translateY(-4px);

    box-shadow:0 14px 30px rgba(15,23,42,.12);

}

.icon-box{

    width:60px;

    height:60px;

    border-radius:16px;

    background:#2563EB;

    color:white;

    display:flex;

    justify-content:center;

    align-items:center;

    font-size:26px;

    flex-shrink:0;

}

.content{

    flex:1;

}

.content h2{

    margin:0;

    font-size:32px;

    font-weight:700;

    color:#0F172A;

    line-height:1;

}

.content p{

    margin-top:8px;

    margin-bottom:0;

    color:#64748B;

    font-size:15px;

    font-weight:500;

}

@media(max-width:768px){

    .stats-card{

        padding:18px;

    }

    .icon-box{

        width:52px;

        height:52px;

        font-size:22px;

    }

    .content h2{

        font-size:26px;

    }

}

</style>