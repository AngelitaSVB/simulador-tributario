import { Component } from '@angular/core';
import { SimuladorComponent } from './simulador/simulador';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [SimuladorComponent], // <- IMPORTA o componente aqui
  templateUrl: './app.html',
})
export class AppComponent {}

