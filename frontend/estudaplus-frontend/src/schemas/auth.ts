import {z} from 'zod'

export const loginSchema = z.object({
  email: z
    .string()
    .min(1, "O email é obrigatório.")
    .email("Email inválido"),
  password: z
    .string()
    .min(1, "A senha é obrigatória.")
    .min(6, "Senha deve ter pelo menos 6 caracteres."),
});

export type SignInForm = z.infer<typeof loginSchema>