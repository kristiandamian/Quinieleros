using System;

namespace Quinieleros.Ligas
{
	public class Zacatecas : EquipoMexico
	{
		public Zacatecas ()
		{
			this.Apodos = new System.Collections.Generic.List<string> (){ "Los mineros", "La marea roja" };
			this.Nombre = "Zacatecas";
			this.Icon = "";
			this.id = "ZACATECAS";
		}
	}
}

