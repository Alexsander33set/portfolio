<script setup>

import { ref, watch } from 'vue'
import { RouterLink } from 'vue-router'
import { useRoute } from 'vue-router'
const route = useRoute()
//* ===== Pinia =====
import { storeToRefs } from 'pinia';
import { useProjectsStore } from '@/stores/projects'
const { projects, isFetchingProjects } = storeToRefs(useProjectsStore())
//* ===== Shadcn =====
import { Breadcrumb, BreadcrumbItem, BreadcrumbLink, BreadcrumbList, BreadcrumbPage, BreadcrumbSeparator,
} from '@/components/ui/breadcrumb'
import { Skeleton } from '@/components/ui/skeleton'
import { Button } from '@/components/ui/button'
import { Badge } from '@/components/ui/badge'
import { Icon } from '@iconify/vue'



const projectID = route.params.name


//* Example
const project = ref(null)

project.value = projects.value.find(proj => proj._id == projectID)

watch(isFetchingProjects, (newVal) => {
  if (newVal === false) {
    console.log("Projects received")
    project.value = projects.value.find(proj => proj._id == projectID)
  }
})

console.log(`Projects ID from URL : ${projectID} with type ${typeof projectID}
        Projects ID 0 : ${projects.value[0]?._id} with type ${typeof projects.value[0]?._id}`)

// const project = getProjects()

const filter = {
  "html": "nonicons:html-16",
  "css": "nonicons:css-16",
  "javascript": "nonicons:javascript-16",
  "typescript": "nonicons:typescript-16",
  "node": "nonicons:node-16",
  "vue": "nonicons:vue-16",
  "vuejs": "nonicons:vue-16",
  "vue3": "nonicons:vue-16",
  "python": "nonicons:python-16",
  "flask": "devicon:flask",
  "java": ":nonicons:java-16",
  "angular": "nonicons:angular-16",
  "tailwind": "devicon:tailwindcss",
  "tailwindcss": "devicon:tailwindcss",
  "eslint": "nonicons:eslint-16",
  "prettier": "nonicons:prettier-16",
  "aws": "vscode-icons:file-type-aws",
  "yaml": "vscode-icons:file-type-aws",
  "yarn": "devicon:yarn",
  "vite": "devicon:vitejs",
  "supabase": "devicon:supabase",
  "sonarqube": "devicon:sonarqube",
  "railway": "devicon:railway",
  "mongodb": "devicon:mongodb"
}
</script>

<template>
  <main class="p-8 flex-1">
    <Breadcrumb>
      <BreadcrumbList>
        <BreadcrumbItem>
          <BreadcrumbLink href="/">
            home
          </BreadcrumbLink>
        </BreadcrumbItem>
        <BreadcrumbSeparator />
        <BreadcrumbItem>
          <BreadcrumbLink href="/projects">
            projects
          </BreadcrumbLink>
        </BreadcrumbItem>
        <BreadcrumbSeparator />
        <BreadcrumbItem>
          <BreadcrumbPage>{{ project ? project.slug : projectID }}</BreadcrumbPage>
        </BreadcrumbItem>
      </BreadcrumbList>
    </Breadcrumb>
    <template v-if="project">
      <section id="proj-presentation" class="flex gap-6 pt-6">
        <div id="proj-image" class="rounded-lg overflow-hidden shadow-md">
          <img class="h-[200px] w-[300px]"
            src="../assets/images/no-image.png"
            alt="example">
        </div>
        <div id="proj-main-text">
          <div id="proj-title-&-privace" class="inline-flex gap-4">
            <h3 class="text-3xl capitalize">
              {{ project.name }}
            </h3>
            <Badge variant="outline">
              {{ project.is_private ? "Private" : "Public" }}
            </Badge>
            <Badge variant="outline">
              {{ project.status ? "Active" : "Inative" }}
            </Badge>
          </div>
          <div id="proj-link" class="text-purple-500 text-primary leading-loose">
            <a :href="project.url" target="_blank" rel="noopener noreferrer">{{ project.url }}</a>
          </div>
          <div id="proj-creation-date" class="leading-loose">
            Created at {{ new Date(project.created_at).toLocaleDateString(undefined, {
              month: 'short',
              year: '2-digit'
            }) }}
          </div>
        </div>
      </section>
      <section id="technologies" class="pt-4">
        <h4 class="text-xl">Technologies:
          <div class="pt-2 inline-flex gap-2">
            <Badge class="capitalize leading-normal inline-flex gap-2" v-for="(tech, i) in project.technologies"
              :key="i">
              <Icon :icon="filter[tech]" class="" />
              {{ tech }}
            </Badge>
          </div>
        </h4>
      </section>
      <section id="proj-description" class="mt-4 p-4 rounded-xl bg-slate-100 dark:bg-slate-900 ">
        <div class="whitespace-pre-wrap min-w-full prose lg:prose-xs flex-1 dark:text-white">
          <!-- class="prose lg:prose-xs" -->
          {{ project.description }}
        </div>

      </section>
    </template>
    <template v-if="project === undefined">
      <div id="not-found">
        {{ $t('projects.notFound') }}
        <RouterLink to="/" >
          <Button variant="outline" class="mt-4 block">{{ $t('button.return') }}</Button>
        </RouterLink>
      </div>
    </template>
    <template v-if="project === null">
      <div>
        <section class="flex gap-6 pt-6">
          <div class="rounded-lg overflow-hidden shadow-md">
            <Skeleton class="w-[300px] h-[200px]" />
          </div>
          <div>
            <div class="inline-flex gap-4">
              <h3 class="text-3xl capitalize">
                <Skeleton class="w-96 h-6" />
              </h3>
              <Skeleton class="w-16 h-6" />
              <Skeleton class="w-16 h-6" />
            </div>
            <div class="leading-loose">
              <Skeleton class="w-16 h-6" />
            </div>
            <div class="leading-loose mt-1">
              <Skeleton class="w-16 h-6" />
            </div>
          </div>
        </section>
        <section id="technologies" class="pt-4">
          <h4 class="text-xl">Technologies:
            <div class="pt-2 inline-flex gap-2">
              <Skeleton class="w-16 h-6" />
              <Skeleton class="w-16 h-6" />
              <Skeleton class="w-16 h-6" />
            </div>
          </h4>
        </section>
        <section class="mt-4 p-4 rounded-xl bg-slate-100 dark:bg-slate-900">
          <div class="min-w-full flex flex-col gap-2 flex-1 dark:text-white">
            <!-- class="prose lg:prose-xs" -->
            <Skeleton class="min-w-max h-6" />
            <Skeleton class="min-w-max h-6" />
            <Skeleton class="min-w-max h-6" />
            <Skeleton class="min-w-max h-6" />
            <Skeleton class="min-w-max h-6" />
          </div>
        </section>
      </div>
    </template>
  </main>
</template>

<style>
#not-found{
  @apply pt-8 text-3xl ;
}

</style>
