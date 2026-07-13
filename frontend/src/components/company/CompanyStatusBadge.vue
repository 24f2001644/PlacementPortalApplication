<template>

<span

    class="badge"

    :class="badgeClass"

>

    {{ status }}

</span>

</template>

<script setup>

import { computed } from "vue"

const props = defineProps({

    status:String

})

const badgeClass = computed(()=>{

    switch(props.status){

        case "Approved":

            return "bg-success"

        case "Rejected":

            return "bg-danger"

        case "Pending":

            return "bg-warning text-dark"

        case "Closed":

            return "bg-secondary"

        case "Selected":

            return "bg-primary"

        case "Shortlisted":

            return "bg-info"

        default:

            return "bg-secondary"

    }

})

</script>

<style scoped>

.badge{

padding:8px 14px;

border-radius:20px;

font-size:13px;

font-weight:600;

}

</style>