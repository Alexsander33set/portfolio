<script setup>
import { ref, computed } from 'vue'
import { storeToRefs } from 'pinia';

import { useProjectsStore } from '@/stores/projects'
const { projects } = storeToRefs(useProjectsStore())
const { deleteProject } = useProjectsStore()

//* ===== Shadcn =====
import { Icon } from '@iconify/vue'
import { Input } from '@/components/ui/input'
import { Textarea } from '@/components/ui/textarea'
import { Button } from '@/components/ui/button'
import { Label } from '@/components/ui/label'
import { Switch } from '@/components/ui/switch'

import {
  Table,
  TableBody,
  // TableCaption,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table'
import { Select,SelectContent,SelectGroup,SelectItem,/*SelectLabel,*/SelectTrigger,SelectValue } from '@/components/ui/select'
import { ComboboxAnchor, ComboboxContent, ComboboxInput, ComboboxPortal, ComboboxRoot } from 'radix-vue'
import { CommandEmpty, CommandGroup, CommandItem, CommandList } from '@/components/ui/command'
import { TagsInput, TagsInputInput, TagsInputItem, TagsInputItemDelete, TagsInputItemText } from '@/components/ui/tags-input'
import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
  AlertDialogTrigger,
} from '@/components/ui/alert-dialog'


//* =============== Projects ===============



//* =============== Projects Operations ===============

function editProject(projectName) {
  console.log("edit: " + projectName)
/**
  [x] Get project name
  [ ] Select the project from the list
  [ ] Populate the form
  [ ] Open  the form
*/
}

function submitDeletion(projectName){
  console.log("submitDeletion")


  /**
   * @param projectName
  * [x] Get project name
  * [ ] Send a double check
  * [ ] Validade
  */
}


//* =============== Form ===============

const form = ref({
  data: {
    name: "",
    description: "",
    image: "",
    url: "",
    github: "",
    isPrivate: false,
    technologies: [],
    frameworks: [],
    status: ""
  },
  isOpen: false,
  process: ""
})

const formDataStructure = {
  name: "",
  description: "",
  image: "",
  url: "",
  github: "",
  isPrivate: false,
  technologies: [],
  frameworks: [],
  status: ""
}

function clearFormData(){
  form.value.data = {...formDataStructure}
}

function fillForm(projectSlug){
  console.log("fillForm")
  console.log(projectSlug)

  let value = projects.value.filter((project) => project.slug == projectSlug)
  console.log(value)
}

function openForm(type, projectSlug=null){
  clearFormData()
  if (projectSlug){fillForm(projectSlug)}
  form.value.process = type
  form.value.isOpen = true
}

function closeForm(){
  clearFormData()
  form.value.isOpen = false
}

function saveForm(){
  switch (form.value.process){
    case "create":
      console.log("create")
      break;
    case "edit":
      console.log("edit")
      break;
    default:
      console.log("No conditions found")
  }
  closeForm()
}

const imageChanged = ref("#")
function changeImage(event) {

  let smg = event.target.files
  imageChanged.value = (URL.createObjectURL(smg[0]))
  console.log(smg)
  console.log(imageChanged.value)
}

const frameworks = [
  { value: 'vue', label: 'Vue 3' },
  { value: 'vite', label: 'Vite' },
  { value: 'nuxt', label: 'Nuxt' },
  { value: 'remix', label: 'Remix' },
  { value: 'astro', label: 'Astro' },
]
const statusList = [
  { value: 'Planning', label: 'Planning' },
  { value: 'Todo', label: 'To do' },
  { value: 'Doing', label: 'Doing' },
  { value: 'Done', label: 'Done' }
]

const modelValue = ref([])
const open = ref(false)
const searchTerm = ref('')

const filteredFrameworks = computed(() => frameworks.filter(i => !modelValue.value.includes(i.label)))
</script>

<template>
  <main class="container flex-1">
    <header class="mt-8">
      <h2 class="text-5xl font-thin">Adminstration Page</h2>
      <hr>
    </header>
    <section v-if="!form.isOpen" class="flex flex-col mt-8 gap-2">
      <h3 class="text-4xl">Projects</h3>

      <Table>
        <TableHeader>
          <TableRow>
            <TableHead class="text-nowrap max-w-60">
              Application Name
            </TableHead>
            <TableHead>Status</TableHead>
            <TableHead>GitHub</TableHead>
            <TableHead>URL</TableHead>
            <TableHead class="text-center">Edit</TableHead>
            <TableHead class="text-center">Delete</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          <TableRow v-for="(project, i) in projects" :key="i">
            <TableCell class="font-medium">
              {{ project.name }}
            </TableCell>
            <TableCell>{{ project.status }}</TableCell>
            <TableCell>
              <template v-if="project.github">
              <a :href="project.github" class="hover:text-blue-500 transition-colors">
                {{ (project.github.split('/')[project.github.split('/').length - 1]) }}
              </a>
              </template>
              <template v-else><p class="text-gray-600">None</p></template>

            </TableCell>
            <TableCell>
              <a v-if="project.url" :href="project.url" class="hover:text-blue-500 transition-colors">
                {{ project.url.replace('https://','')}}
              </a>
              <p v-else class="text-gray-600">None</p>
            </TableCell>
            <TableCell class="text-center">
              <Button @click="openForm('edit', project.slug)" variant="outline">
                <Icon icon="mdi:edit-outline" class="-m-1 scale-125" />
              </Button>
            </TableCell>
            <TableCell class="text-center">
              <AlertDialog>
                <AlertDialogTrigger>
                  <Button variant="outline">
                    <Icon icon="mdi:delete-outline" class="-m-1 scale-125 text-red-600 dark:text-red-400" />
                  </Button>
                </AlertDialogTrigger>
                <AlertDialogContent>
                  <AlertDialogHeader>
                    <AlertDialogTitle>{{ $t('confirmDelition.title') }}</AlertDialogTitle>
                    <AlertDialogDescription>
                      {{ $t('confirmDelition.description') }}
                    </AlertDialogDescription>
                  </AlertDialogHeader>
                  <AlertDialogFooter>
                    <AlertDialogCancel>{{ $t('confirmDelition.cancel') }}</AlertDialogCancel>
                    <AlertDialogAction @click="deleteProject(project._id)">{{ $t('confirmDelition.confirm') }}</AlertDialogAction>
                  </AlertDialogFooter>
                </AlertDialogContent>
              </AlertDialog>
            </TableCell>
          </TableRow>
        </TableBody>
      </Table>
      <div class="h-10">
        <span class="float-right">
          <Button @click="openForm('create')" class="flex gap-2 items-center p-2">
            <Icon icon="mdi:plus-circle-otline" /> Add Project
          </Button>
        </span>
      </div>
    </section>

    <form v-if="form.isOpen" class="my-10">
      <h3 class="text-3xl">Change App</h3>
      <section class="border p-4 mt-4 flex flex-col gap-2 rounded-md">
        <div class="flex items-center gap-1.5">
          <Label for="name">Name:</Label>
          <Input id="name" type="text" v-model="form.data.name" placeholder="Project Name" />
          <Select>
            <SelectTrigger class="w-[180px]">
              <SelectValue placeholder="Status" />
            </SelectTrigger>
            <SelectContent>
              <SelectGroup>
                <SelectItem v-for="(status, index) in statusList" :key="index" :value="status.value">
                  {{ status.label }}
                </SelectItem>
              </SelectGroup>
            </SelectContent>
          </Select>
        </div>
        <section class="border rounded-sm my-1 p-4 py-2 transition-all delay-150 duration-500 flex flex-col gap-2">
            <div class="flex gap-2 items-center">
              <h5>Is Private?</h5>
              <Switch v-model="form.data.isPrivate" @click="form.data.isPrivate = !form.data.isPrivate" />
            </div>
            <section v-if="!form.data.isPrivate" class="flex flex-col gap-2 mt-2">
              <div>
                <Label for="url">URL</Label>
                <Input id="url" type="text" v-model="form.data.url" placeholder="https://url.com" />
              </div>
              <div>
                <Label for="github">GitHub</Label>
                <Input id="github" type="text" v-model="form.data.github"
                  placeholder="https://github.com/Alexsander33set/..." />
              </div>
            </section>
        </section>
        <div class="grid items-center gap-1.5">
          <Label for="description">Description</Label>
          <Textarea id="description" v-model="form.data.description" placeholder="Project Description" />
        </div>
        <div class="grid items-center gap-1.5">
          <Label for="name">Technologies</Label>
          <TagsInput class="px-0 gap-0 w-100" :model-value="modelValue">
            <div class="flex gap-2 flex-wrap items-center px-3">
              <TagsInputItem v-for="item in modelValue" :key="item" :value="item">
                <TagsInputItemText />
                <TagsInputItemDelete />
              </TagsInputItem>
            </div>

            <ComboboxRoot v-model="modelValue" v-model:open="open" v-model:searchTerm="searchTerm" class="w-full">
              <ComboboxAnchor as-child>
                <ComboboxInput placeholder="Programming Language, Library, Framework..." as-child>
                  <TagsInputInput class="w-full px-3" :class="modelValue.length > 0 ? 'mt-2' : ''"
                    @keydown.enter.prevent />
                </ComboboxInput>
              </ComboboxAnchor>

              <ComboboxPortal>
                <ComboboxContent>
                  <CommandList position="popper"
                    class="w-[--radix-popper-anchor-width] rounded-md mt-2 border bg-popover text-popover-foreground shadow-md outline-none data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2">
                    <CommandEmpty />
                    <CommandGroup>
                      <CommandItem v-for="framework in filteredFrameworks" :key="framework.value"
                        :value="framework.label" @select.prevent="(ev) => {
                          if (typeof ev.detail.value === 'string') {
                            searchTerm = ''
                            modelValue.push(ev.detail.value)
                          }

                          if (filteredFrameworks.length === 0) {
                            open = false
                          }
                        }">
                        {{ framework.label }}
                      </CommandItem>
                    </CommandGroup>
                  </CommandList>
                </ComboboxContent>
              </ComboboxPortal>
            </ComboboxRoot>
          </TagsInput>
        </div>
        <div class="grid w-full max-w-sm items-center gap-1.5">
          <Label for="created_at">Iniciado em</Label>
          <Input id="created_at" type="date" v-model="form.data.created_at" placeholder="dd/mm/aaaa" />
        </div>
        <div class="grid w-full max-w-sm items-center gap-1.5">
          <Label for="picture">Foto</Label>
          <Input id="picture" type="file" accept="image/*" @change="changeImage" />
          <template v-if="form.data.image">
            <div>
              <p>Preview</p>
              <img :src="imageChanged" alt="pho">
            </div>
          </template>
        </div>
      </section>
      <section class="mt-2 flex justify-end gap-4">
        <Button class="float-right" type="reset" @click="closeForm()">Cancel</Button>
        <Button class="float-right" type="submit" @click="saveForm()">Save</Button>
      </section>
    </form>
  </main>
</template>
