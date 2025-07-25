import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient, HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-simulador',
  standalone: true,
  imports: [CommonModule, FormsModule, HttpClientModule],
  templateUrl: './simulador.html',
  styleUrls: ['./simulador.css'],
})
export class SimuladorComponent {
  receita_comercio: number = 0;
  receita_servico: number = 0;
  folha_pagamento: number = 0;
  despesas_anuais: number = 0;
  resultado: any = null;
  erro: string = '';

  // URL do backend na AWS
  readonly endpoint = 'http://simulador-tributario-env.eba-kxrfbazi.us-east-1.elasticbeanstalk.com/calcular';

  constructor(private http: HttpClient) {}

  calcular() {
    const payload = {
      receita_comercio: this.receita_comercio,
      receita_servico: this.receita_servico,
      folha_pagamento: this.folha_pagamento,
      despesas_anuais: this.despesas_anuais
    };

    this.http.post(this.endpoint, payload).subscribe({
      next: (res: any) => {
        this.resultado = res;
        this.erro = '';
      },
      error: (err) => {
        this.erro = 'Erro ao calcular. Tente novamente.';
        console.error(err);
      }
    });
  }
}
