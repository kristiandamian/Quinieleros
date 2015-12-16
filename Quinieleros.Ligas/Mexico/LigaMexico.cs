using System;
using System.Collections.Generic;

namespace Quinieleros.Ligas
{
	public class LigaMexico : LigaBase
	{
		new public List<EquipoMexico> Equipos { get; set; }
		public LigaMexico ()
		{
			this.NombreLiga = "Liga Bancomer MX";
			this.Pais = "México";
			this.Equipos = getEquipos ();
		}

		List<EquipoMexico> getEquipos()
		{
			var equipos = new List<EquipoMexico> ();
			//PRIMERA
			equipos.Add (new Pumas ());

			return equipos;
		}
	}

	public class EquipoMexico : EquipoBase
	{
	}
}

