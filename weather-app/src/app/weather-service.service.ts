import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import {days, hours, city} from './weather'
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class WeatherServiceService {

  BASE_URL = `http://127.0.0.1:5000`

  constructor(
    private http: HttpClient
  ) { }

  getWeatherDays(): Observable<days[]>{
    return this.http.get<days[]>(this.BASE_URL)
  }

  postCity(city:string): Observable<city>{
    return this.http.post<city>(this.BASE_URL, {city})
  }
}
