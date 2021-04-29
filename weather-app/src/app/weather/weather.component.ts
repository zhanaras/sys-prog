import { Component, OnInit } from '@angular/core';
import { days, hours, city } from '../weather';
import { WeatherServiceService } from '../weather-service.service';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';
import { first } from 'rxjs/operators';

@Component({
  selector: 'app-weather',
  templateUrl: './weather.component.html',
  styleUrls: ['./weather.component.css']
})
export class WeatherComponent implements OnInit {

  days: days[] = []
  searchStr: string;

  constructor(
    public weatherService: WeatherServiceService,
  ) { }

  ngOnInit(): void {
    this.getWeatherDays()
  }

  getWeatherDays(){
    this.weatherService.getWeatherDays().subscribe(days => {this.days = days;})
  }

  postCity(){
    this.weatherService.postCity(this.searchStr).subscribe()
  }

}
