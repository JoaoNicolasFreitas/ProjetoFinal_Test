import { useState } from "react";
import { useForm, Controller } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";
import * as yup from "yup";
import "./App.css";

const schema = yup.object().shape({
  nome: yup
    .string()
    .required("Nome é obrigatório")
    .min(3, "Nome deve ter no mínimo 3 caracteres")
    .max(50, "Nome deve ter no máximo 50 caracteres"),
  telefone: yup
    .string()
    .required("Telefone é obrigatório")
    .matches(/^\(\d{2}\) \d{5}-\d{4}$/, "Formato inválido"),
  cpf: yup
    .string()
    .required("CPF é obrigatório")
    .matches(/^\d{3}\.\d{3}\.\d{3}-\d{2}$/, "Formato inválido")
    .test("cpf", "CPF inválido", (value) => {
      if (!value) return false;
      const cpf = value.replace(/[^\d]/g, "");
      if (cpf.length !== 11) return false;
      if (/^(\d)\1{10}$/.test(cpf)) return false;

      let sum = 0;
      for (let i = 0; i < 9; i++) {
        sum += parseInt(cpf.charAt(i)) * (10 - i);
      }
      let rest = 11 - (sum % 11);
      const digit1 = rest > 9 ? 0 : rest;

      sum = 0;
      for (let i = 0; i < 10; i++) {
        sum += parseInt(cpf.charAt(i)) * (11 - i);
      }
      rest = 11 - (sum % 11);
      const digit2 = rest > 9 ? 0 : rest;

      return (
        digit1 === parseInt(cpf.charAt(9)) &&
        digit2 === parseInt(cpf.charAt(10))
      );
    }),
  email: yup.string().required("Email é obrigatório").email("Email inválido"),
  senha: yup
    .string()
    .required("Senha é obrigatória")
    .min(8, "Senha deve ter no mínimo 8 caracteres")
    .max(20, "Senha deve ter no máximo 20 caracteres"),
  confirmarEmail: yup
    .string()
    .required("Confirmação de email é obrigatória")
    .oneOf([yup.ref("email")], "Emails não conferem"),
  confirmarSenha: yup
    .string()
    .required("Confirmação de senha é obrigatória")
    .oneOf([yup.ref("senha")], "Senhas não conferem"),
});

type FormData = yup.InferType<typeof schema>;

function App() {
  const [success, setSuccess] = useState(false);
  const {
    control,
    handleSubmit,
    formState: { errors },
    trigger,
    setValue,
  } = useForm<FormData>({
    resolver: yupResolver(schema),
    mode: "onChange",
    reValidateMode: "onChange",
  });

  const formatPhone = (value: string) => {
    const numbers = value.replace(/\D/g, "");
    if (numbers.length <= 11) {
      return numbers.replace(/(\d{2})(\d{5})(\d{4})/, "($1) $2-$3");
    }
    return value;
  };

  const formatCPF = (value: string) => {
    const numbers = value.replace(/\D/g, "");
    if (numbers.length <= 11) {
      return numbers.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/, "$1.$2.$3-$4");
    }
    return value;
  };

  const onSubmit = (data: FormData) => {
    console.log(data);
    setSuccess(true);
  };

  const handleFieldChange = (
    field: keyof FormData,
    value: string,
    onChange: (value: string) => void
  ) => {
    onChange(value);
    setValue(field, value, { shouldValidate: true });
  };

  return (
    <div className="container py-5">
      <div className="row justify-content-center">
        <div className="col-md-8 col-lg-6">
          <div className="card">
            <div className="card-body p-4 p-md-5">
              <div className="text-center mb-4">
                <h2 className="card-title">Cadastro</h2>
                <p className="text-muted">
                  Preencha os dados abaixo para criar sua conta
                </p>
              </div>

              {success && (
                <div className="alert alert-success" role="alert">
                  <i className="bi bi-check-circle-fill me-2"></i>
                  Cadastro realizado com sucesso!
                </div>
              )}

              <form
                onSubmit={handleSubmit(onSubmit)}
                data-testid="registration-form"
              >
                <div className="row">
                  <div className="col-md-12 mb-3">
                    <Controller
                      name="nome"
                      control={control}
                      render={({ field }) => (
                        <>
                          <label htmlFor="nome" className="form-label">
                            <i className="bi bi-person me-2"></i>
                            Nome Completo
                          </label>
                          <input
                            {...field}
                            type="text"
                            className={`form-control ${
                              errors.nome ? "is-invalid" : ""
                            }`}
                            id="nome"
                            placeholder="Digite seu nome completo"
                            data-testid="nome-input"
                          />
                          {errors.nome && (
                            <div
                              className="invalid-feedback"
                              data-testid="nome-error"
                            >
                              {errors.nome.message}
                            </div>
                          )}
                        </>
                      )}
                    />
                  </div>

                  <div className="col-md-6 mb-3">
                    <Controller
                      name="telefone"
                      control={control}
                      render={({ field }) => (
                        <>
                          <label htmlFor="telefone" className="form-label">
                            <i className="bi bi-telephone me-2"></i>
                            Telefone
                          </label>
                          <input
                            {...field}
                            type="text"
                            className={`form-control ${
                              errors.telefone ? "is-invalid" : ""
                            }`}
                            id="telefone"
                            placeholder="(00) 00000-0000"
                            maxLength={15}
                            data-testid="telefone-input"
                            onChange={(e) => {
                              const formatted = formatPhone(e.target.value);
                              handleFieldChange(
                                "telefone",
                                formatted,
                                field.onChange
                              );
                            }}
                          />
                          {errors.telefone && (
                            <div
                              className="invalid-feedback"
                              data-testid="telefone-error"
                            >
                              {errors.telefone.message}
                            </div>
                          )}
                        </>
                      )}
                    />
                  </div>

                  <div className="col-md-6 mb-3">
                    <Controller
                      name="cpf"
                      control={control}
                      render={({ field }) => (
                        <>
                          <label htmlFor="cpf" className="form-label">
                            <i className="bi bi-person-badge me-2"></i>
                            CPF
                          </label>
                          <input
                            {...field}
                            type="text"
                            className={`form-control ${
                              errors.cpf ? "is-invalid" : ""
                            }`}
                            id="cpf"
                            placeholder="000.000.000-00"
                            maxLength={14}
                            data-testid="cpf-input"
                            onChange={(e) => {
                              const formatted = formatCPF(e.target.value);
                              handleFieldChange(
                                "cpf",
                                formatted,
                                field.onChange
                              );
                            }}
                          />
                          {errors.cpf && (
                            <div
                              className="invalid-feedback"
                              data-testid="cpf-error"
                            >
                              {errors.cpf.message}
                            </div>
                          )}
                        </>
                      )}
                    />
                  </div>

                  <div className="col-md-6 mb-3">
                    <Controller
                      name="email"
                      control={control}
                      render={({ field }) => (
                        <>
                          <label htmlFor="email" className="form-label">
                            <i className="bi bi-envelope me-2"></i>
                            Email
                          </label>
                          <input
                            {...field}
                            type="email"
                            className={`form-control ${
                              errors.email ? "is-invalid" : ""
                            }`}
                            id="email"
                            placeholder="seu@email.com"
                            data-testid="email-input"
                            onChange={(e) => {
                              handleFieldChange(
                                "email",
                                e.target.value,
                                field.onChange
                              );
                              trigger("confirmarEmail");
                            }}
                          />
                          {errors.email && (
                            <div
                              className="invalid-feedback"
                              data-testid="email-error"
                            >
                              {errors.email.message}
                            </div>
                          )}
                        </>
                      )}
                    />
                  </div>

                  <div className="col-md-6 mb-3">
                    <Controller
                      name="confirmarEmail"
                      control={control}
                      render={({ field }) => (
                        <>
                          <label
                            htmlFor="confirmarEmail"
                            className="form-label"
                          >
                            <i className="bi bi-envelope-check me-2"></i>
                            Confirmar Email
                          </label>
                          <input
                            {...field}
                            type="email"
                            className={`form-control ${
                              errors.confirmarEmail ? "is-invalid" : ""
                            }`}
                            id="confirmarEmail"
                            placeholder="seu@email.com"
                            data-testid="confirmar-email-input"
                            onChange={(e) => {
                              handleFieldChange(
                                "confirmarEmail",
                                e.target.value,
                                field.onChange
                              );
                            }}
                          />
                          {errors.confirmarEmail && (
                            <div
                              className="invalid-feedback"
                              data-testid="confirmar-email-error"
                            >
                              {errors.confirmarEmail.message}
                            </div>
                          )}
                        </>
                      )}
                    />
                  </div>

                  <div className="col-md-6 mb-3">
                    <Controller
                      name="senha"
                      control={control}
                      render={({ field }) => (
                        <>
                          <label htmlFor="senha" className="form-label">
                            <i className="bi bi-lock me-2"></i>
                            Senha
                          </label>
                          <input
                            {...field}
                            type="password"
                            className={`form-control ${
                              errors.senha ? "is-invalid" : ""
                            }`}
                            id="senha"
                            placeholder="Digite sua senha"
                            data-testid="senha-input"
                            onChange={(e) => {
                              handleFieldChange(
                                "senha",
                                e.target.value,
                                field.onChange
                              );
                              trigger("confirmarSenha");
                            }}
                          />
                          {errors.senha && (
                            <div
                              className="invalid-feedback"
                              data-testid="senha-error"
                            >
                              {errors.senha.message}
                            </div>
                          )}
                        </>
                      )}
                    />
                  </div>

                  <div className="col-md-6 mb-4">
                    <Controller
                      name="confirmarSenha"
                      control={control}
                      render={({ field }) => (
                        <>
                          <label
                            htmlFor="confirmarSenha"
                            className="form-label"
                          >
                            <i className="bi bi-lock-fill me-2"></i>
                            Confirmar Senha
                          </label>
                          <input
                            {...field}
                            type="password"
                            className={`form-control ${
                              errors.confirmarSenha ? "is-invalid" : ""
                            }`}
                            id="confirmarSenha"
                            placeholder="Confirme sua senha"
                            data-testid="confirmar-senha-input"
                            onChange={(e) => {
                              handleFieldChange(
                                "confirmarSenha",
                                e.target.value,
                                field.onChange
                              );
                            }}
                          />
                          {errors.confirmarSenha && (
                            <div
                              className="invalid-feedback"
                              data-testid="confirmar-senha-error"
                            >
                              {errors.confirmarSenha.message}
                            </div>
                          )}
                        </>
                      )}
                    />
                  </div>
                </div>

                <button
                  type="submit"
                  className="btn btn-primary w-100 py-3"
                  data-testid="submit-button"
                >
                  <i className="bi bi-person-plus me-2"></i>
                  Criar Conta
                </button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;