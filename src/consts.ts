export type Site = {
  TITLE: string
  DESCRIPTION: string
  EMAIL: string
  NUM_POSTS_ON_HOMEPAGE: number
  POSTS_PER_PAGE: number
  SITEURL: string
}

export type Link = {
  href: string
  label: string
}

export const SITE: Site = {
  TITLE: 'Main',
  DESCRIPTION:
    'Web de informacion ',
  EMAIL: 'lit.io30303@gmail.com',
  NUM_POSTS_ON_HOMEPAGE: 2,
  POSTS_PER_PAGE: 3,
  SITEURL: 'https://lllit.reflex.run/',
}

export const NAV_LINKS: Link[] = [
  { href: '/blog', label: 'Tecnologias' },
  { href: '/authors', label: 'Autores' },
  { href: '/about', label: 'Sobre' },
  { href: '/tags', label: 'tags' },
]

export const SOCIAL_LINKS: Link[] = [
  { href: 'https://github.com/lllit', label: 'GitHub' },
  { href: 'lit.io30303@gmail.com', label: 'Email' },
]
