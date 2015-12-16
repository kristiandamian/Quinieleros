using System;

namespace Quinieleros.Ligas
{
	public class Monterrey : EquipoMexico
	{
		public Monterrey ()
		{
			this.Apodos = new System.Collections.Generic.List<string> (){ "Los rayados","La pandilla" };
			this.Nombre = "Monterrey";
			this.Icon = "";
			this.id = "MONTERREY";
		}
	}
}

