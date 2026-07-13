<script setup>

import { computed } from "vue"

const props = defineProps({

status:String

})

const badgeClass=computed(()=>{

switch(props.status){

case "Approved":

return "bg-success"

case "Pending":

return "bg-warning text-dark"

case "Rejected":

return "bg-danger"

case "Closed":

return "bg-secondary"

case "Selected":

return "bg-success"

case "Shortlisted":

return "bg-primary"

case "Applied":

return "bg-info"

default:

return "bg-secondary"

}

})

</script>

<template>

<span

class="badge rounded-pill"

:class="badgeClass"

>

{{ status }}

</span>

</template>